# Week of 12 October: parent's sheet

Both kids start at rank 0, full support: checkpoint at 12:00, teach-back on every subject done that day, version history on every doc. How to talk about it: `curriculum/routine.md`, "How to talk about it".

## Before Monday

- Print 5 day sheets per kid (`weeks/day_sheet.md`).
- Make sure both have Khan / Oak access (Khan: signed-in account; optionally link a parent account to see their progress).
- Decide where phones go during the day, and say it once, plainly.
- Optional: send the reading files to the Kindle (EPUB in each topic folder, once built).

## Each day

| Time | You | Takes |
|---|---|---|
| 08:45 | Initial both day sheets. Monday: watch them create and share the five Google Docs. | 10 min (Mon 20) |
| 12:00 | Checkpoint: "Anything to flag?", then maths and core 2 docs (see table below), version history on both, teach-back on both subjects. | 20 min |
| 16:00 | Close: "Anything to flag?", "What was the most interesting thing today?", teach-back on the two afternoon subjects, look at one self-marked item each, phones back. | 15-20 min |
| 16:15 | Family PE, 30 minutes; take turns choosing what. Then log both kids in `progress/log.csv`, run `python3 tools/progress.py status`, and tell them tomorrow's support. | 35 min |

On full support the afternoon subjects get their teach-back at the close, since there's no 14:00 checkpoint.

## What's due at 12:00

| Day | Matt maths | Sarah maths | Core 2 (both) |
|---|---|---|---|
| Mon | Algebraic equations basics | Oak lessons 1-2 | English: Part 1 bullets, Q2, a two-sentence guess |
| Tue | One-step equations intuition | Oak lesson 3 | Science: Part 1 bullets, Q1-3 |
| Wed | One-step add & subtract | Oak lesson 4 | English: Q1, Q3, Q4, guess check |
| Thu | One-step multiply & divide | Oak lesson 5 | Science: Part 2 bullets, Q4-5 |
| Fri | Finding mistakes + self-test 1, self-marked | Self-test 1 self-marked + Oak lesson 6 | English: Part 2 bullets, Q6-7 |

Afternoons (both kids, checked at 16:00): see the "Done when" column in `week.md` (the "This week" page on the progress board).

## Teach-back questions

From each topic's `key.md`, section "Verbal check questions". Pick one from the key and ask one about their own writing ("explain this sentence in different words"). Don't ask the same key question twice in a week.

## Friday

- 16:00-16:45 weekly close, then family PE at 16:45. Do the baseline retry with Sarah (see `topics/maths/uk_01_place_value/key.md`).
- Read the four Friday lines with each kid, separately. Line 4 ("this week shows I'm someone who...") is theirs: ask about it, don't correct it.
- A kid with 5 self-run days out of 6 reaches rank 1: mark it the way they choose. Not there yet: say what they did manage, with the evidence.
- Weekend with Claude: update logs and profiles, publish the progress board (`python3 tools/progress.py publish`), prepare week B materials (self-test 2s, week plans).
