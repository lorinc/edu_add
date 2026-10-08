"""Compute rank and support from progress/log.csv, and build the public site.

Usage:
  python3 tools/progress.py status         # rank, tomorrow's support, self-run days, per kid
  python3 tools/progress.py site <outdir>  # write index.html + data.json (pseudonyms only)
  python3 tools/progress.py publish        # build into site_public/ and push to the public repo

log.csv columns (one row per kid per school day):
  date             YYYY-MM-DD
  student          us | uk
  plan_ok          Y/N  day sheet filled in by 10:00
  morning_done     Y/N  everything due at the checkpoint was done
  teachback_asked  number of teach-back questions asked
  teachback_ok     number explained in their own words
  shortcut         0 none, 1 small, 2 a block, 3 a pattern (curriculum/routine.md)
  flagged          Y/N/- the kid flagged it themselves (- = no shortcut)
  selfmark_done    Y/N/- (- = nothing to self-mark)
  pe               Y/N
  est_min          total estimated minutes on the day sheet
  actual_min       total actual minutes
  again_mistakes   number of "again" mistakes in self-marking
  note             private, never published

Rules (curriculum/routine.md, "Rank and support"):
  Rank is earned (N self-run days out of the last M) and never goes down.
  Support follows rank (0 full, 1 medium, 2 light). It tightens one step
  after an unfinished morning or a block shortcut found by the parent, and
  goes to full after a pattern; it returns to the rank's level after
  regain_after self-run days. Flagged shortcuts never change support.
"""

import csv
import json
import posixpath
import re
import shutil
import subprocess
import sys
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent.parent
PROGRESS = ROOT / "progress"
CONFIG = json.loads((PROGRESS / "site.json").read_text())
SUPPORT = ["full", "medium", "light"]  # index = the rank it belongs to


def yes(v):
    return v.strip().upper() == "Y"


def read_csv(name):
    with open(PROGRESS / name, newline="") as f:
        return list(csv.DictReader(f))


def is_self_run(r):
    shortcut = int(r["shortcut"] or 0)
    return (
        yes(r["plan_ok"])
        and yes(r["morning_done"])
        and int(r["teachback_ok"] or 0) >= int(r["teachback_asked"] or 0)
        and (shortcut == 0 or (shortcut == 1 and yes(r["flagged"])))
        and r["selfmark_done"].strip().upper() in ("Y", "-")
        and yes(r["pe"])
    )


def parts_met(r):
    """How many of the five visible parts of a self-run day were met (shortcuts not counted)."""
    return sum([
        yes(r["plan_ok"]),
        yes(r["morning_done"]),
        int(r["teachback_ok"] or 0) >= int(r["teachback_asked"] or 0),
        r["selfmark_done"].strip().upper() in ("Y", "-"),
        yes(r["pe"]),
    ])


def replay(rows):
    """Apply the rules day by day. Returns per-day records and the current state."""
    rank, support, regain = 0, 0, 0
    window = []  # self-run flags since the last rank-up, newest last
    days = []
    for r in sorted(rows, key=lambda r: r["date"]):
        rank_today, support_today = rank, support
        self_run = is_self_run(r)
        shortcut = int(r["shortcut"] or 0)
        found = shortcut if shortcut and not yes(r["flagged"]) else 0

        # Support: tighten after a hard day, return after self-run days.
        if found == 3:
            support, regain = 0, 0
        elif not yes(r["morning_done"]) or found == 2:
            support, regain = max(support - 1, 0), 0
        elif self_run and support < rank:
            regain += 1
            if regain >= CONFIG["regain_after"]:
                support = rank

        # Rank: earned with most days, never lost.
        window.append(self_run)
        need = CONFIG["rank_after"].get(str(rank))
        if need and sum(window[-need["of"]:]) >= need["days"]:
            if support == rank:
                support = rank + 1
            rank, window = rank + 1, []

        est, act = int(r["est_min"] or 0), int(r["actual_min"] or 0)
        days.append({
            "date": r["date"],
            "rank": rank_today,
            "support": SUPPORT[support_today],
            "self_run": self_run,
            "parts": parts_met(r),
            "morning_done": yes(r["morning_done"]),
            "teachback_asked": int(r["teachback_asked"] or 0),
            "teachback_ok": int(r["teachback_ok"] or 0),
            "estimate_error": round(abs(est - act) / act * 100) if act else None,
            "again_mistakes": int(r["again_mistakes"] or 0),
            "shortcut": shortcut,
            "flagged": yes(r["flagged"]),
        })

    need = CONFIG["rank_after"].get(str(rank))
    return days, {
        "rank": rank,
        "support_tomorrow": SUPPORT[support],
        "self_run_total": sum(d["self_run"] for d in days),
        "self_run_last_10": sum(d["self_run"] for d in days[-10:]),
        "next_rank": None if not need else {
            "rank": rank + 1, "days": need["days"], "of": need["of"],
            "have": sum(window[-need["of"]:]),
        },
    }


def by_student():
    rows = read_csv("log.csv")
    tests = read_csv("tests.csv")
    out = {}
    for key in CONFIG["pseudonyms"]:
        days, now = replay([r for r in rows if r["student"] == key])
        out[key] = {
            "name": CONFIG["pseudonyms"][key],
            "now": now,
            "topics": CONFIG.get("current_topics", {}).get(key, {}),
            "days": days,
            "tests": [
                {k: t[k] for k in ("date", "subject", "topic", "score", "max")}
                for t in tests if t["student"] == key
            ],
        }
    return out


def status():
    for key, s in by_student().items():
        n, days = s["now"], s["days"]
        line = (f"{key}: rank {n['rank']}, support tomorrow: {n['support_tomorrow']}, "
                f"self-run days {n['self_run_total']} (last 10: {n['self_run_last_10']})")
        if n["next_rank"]:
            nr = n["next_rank"]
            line += f"; rank {nr['rank']}: {nr['have']} of {nr['days']} self-run days needed in the last {nr['of']}"
        flagged = sum(1 for d in days if d["shortcut"] and d["flagged"])
        found = sum(1 for d in days if d["shortcut"] and not d["flagged"])
        print(line + f"; shortcuts flagged by the kid {flagged}, found by you {found}")


def site(outdir):
    out = Path(outdir)
    out.mkdir(parents=True, exist_ok=True)
    students = list(by_student().values())
    for st in students:  # shortcuts, flags and support stay between parent and kid
        st["now"].pop("support_tomorrow")
        for d in st["days"]:
            for k in ("shortcut", "flagged", "support"):
                d.pop(k)
    data = {"school_start": CONFIG["school_start"], "students": students}
    (out / "data.json").write_text(json.dumps(data, indent=1))
    shutil.copy(ROOT / "site" / "index.html", out / "index.html")
    shutil.copy(ROOT / "site" / "style.css", out / "style.css")
    (out / "week.html").write_text(week_page())
    for f in ("data.json", "week.html"):
        text = (out / f).read_text()
        leaked = [n for n in CONFIG["private_names"] if re.search(rf"\b{n}\b", text)]
        if leaked:
            sys.exit(f"Refusing to publish: {f} contains {leaked}")
    print(f"Wrote {out}/index.html, week.html, style.css and data.json")


def week_page():
    """Render weeks/<current_week>/week.md; relative links point to the private repo on GitHub."""
    folder = f"weeks/{CONFIG['current_week']}"
    text = (ROOT / folder / "week.md").read_text()
    title = re.search(r"^# (.+)$", text, re.M).group(1)
    base = f"https://github.com/{CONFIG['private_repo']}/blob/main/"

    def link(m):
        target = m.group(2)
        if target.startswith("../"):
            path, _, anchor = target.partition("#")
            target = base + posixpath.normpath(posixpath.join(folder, path)) + (f"#{anchor}" if anchor else "")
        return f"]({target})"

    text = re.sub(r"\]\((\s*)([^)\s]+)\)", link, text)
    body = markdown.markdown(text, extensions=["tables", "toc", "md_in_html"])
    body = re.sub(r'<a href="https://', '<a target="_blank" rel="noopener" href="https://', body)
    # Answer files: the link only opens during self-marking (soft gate, see week_template.html).
    body = re.sub(r'<a target="_blank" rel="noopener" href="([^"]*_answers\.md)">([^<]*)</a>',
                  r'<a class="timed" target="_blank" rel="noopener" data-href="\1">\2</a>', body)
    template = (ROOT / "site" / "week_template.html").read_text()
    return template.replace("{{TITLE}}", title).replace("{{CONTENT}}", body)


def publish():
    """Rebuild the board in site_public/ (a clone of the public repo) and push it."""
    # The week page links into the private repo: warn if those files aren't on GitHub yet.
    private = lambda *a: subprocess.run(["git", "-C", str(ROOT), *a], capture_output=True, text=True).stdout
    unpushed = private("status", "--porcelain", "--", "topics", "weeks", "curriculum").strip()
    ahead = private("rev-list", "--count", "@{u}..HEAD").strip()
    if unpushed or ahead not in ("", "0"):
        print("Warning: some linked files aren't pushed to the private repo yet, so their links "
              "on the week page will be broken. Commit and push edu_add.")
    out = ROOT / "site_public"
    site(out)
    git = lambda *a: subprocess.run(["git", "-C", str(out), *a], check=True, capture_output=True, text=True)
    git("add", "index.html", "week.html", "style.css", "data.json")
    if not git("status", "--porcelain").stdout.strip():
        print("No changes to publish.")
        return
    git("commit", "-m", "Update progress board")
    git("push")
    print(f"Published: {CONFIG['public_url']}")


if __name__ == "__main__":
    if len(sys.argv) >= 2 and sys.argv[1] == "status":
        status()
    elif len(sys.argv) == 3 and sys.argv[1] == "site":
        site(sys.argv[2])
    elif len(sys.argv) == 2 and sys.argv[1] == "publish":
        publish()
    else:
        sys.exit(__doc__)
