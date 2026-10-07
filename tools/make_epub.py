"""Build an EPUB for the Kindle from a topic's Markdown files.

Usage: python3 tools/make_epub.py topics/science/01_earths_moving_surface

Bundles reading.md, tasks.md (if present) and questions.md, in that order,
into <topic>/<topic-name>.epub. Never includes key.md. Send the EPUB to the
Kindle with Amazon's Send to Kindle.
"""

import html
import re
import sys
import uuid
import zipfile
from pathlib import Path

import markdown

PARTS = ["reading.md", "plan.md", "tasks.md", "questions.md"]

CSS = """body { font-family: serif; line-height: 1.5; }
h1, h2, h3 { font-family: sans-serif; }
table { border-collapse: collapse; margin: 1em 0; }
th, td { border: 1px solid #888; padding: 0.3em 0.5em; vertical-align: top; }
blockquote { margin-left: 1.5em; font-style: italic; }
"""


def xhtml(title, body):
    return f"""<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops">
<head><title>{html.escape(title)}</title><link rel="stylesheet" href="style.css"/></head>
<body>
{body}
</body>
</html>
"""


def build(topic_dir: Path) -> Path:
    chapters = []
    for name in PARTS:
        path = topic_dir / name
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        title = re.search(r"^# (.+)$", text, re.M).group(1)
        body = markdown.markdown(text, extensions=["tables"], output_format="xhtml")
        chapters.append((f"ch{len(chapters) + 1}.xhtml", title, body))
    if not chapters:
        sys.exit(f"No Markdown files found in {topic_dir}")

    book_title = chapters[0][1]
    out = topic_dir / f"{topic_dir.name}.epub"
    book_id = f"urn:uuid:{uuid.uuid5(uuid.NAMESPACE_URL, str(topic_dir))}"

    manifest = "\n".join(
        f'<item id="c{i}" href="{f}" media-type="application/xhtml+xml"/>'
        for i, (f, _, _) in enumerate(chapters)
    )
    spine = "\n".join(f'<itemref idref="c{i}"/>' for i in range(len(chapters)))
    nav_items = "\n".join(f'<li><a href="{f}">{html.escape(t)}</a></li>' for f, t, _ in chapters)

    opf = f"""<?xml version="1.0" encoding="utf-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="id">
<metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
<dc:identifier id="id">{book_id}</dc:identifier>
<dc:title>{html.escape(book_title)}</dc:title>
<dc:language>en</dc:language>
<meta property="dcterms:modified">2026-01-01T00:00:00Z</meta>
</metadata>
<manifest>
<item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>
<item id="css" href="style.css" media-type="text/css"/>
{manifest}
</manifest>
<spine>
{spine}
</spine>
</package>
"""
    nav = xhtml("Contents", f'<nav epub:type="toc"><h1>Contents</h1><ol>{nav_items}</ol></nav>')
    container = """<?xml version="1.0" encoding="utf-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
<rootfiles><rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/></rootfiles>
</container>
"""
    with zipfile.ZipFile(out, "w") as z:
        z.writestr("mimetype", "application/epub+zip", compress_type=zipfile.ZIP_STORED)
        z.writestr("META-INF/container.xml", container, compress_type=zipfile.ZIP_DEFLATED)
        z.writestr("OEBPS/content.opf", opf, compress_type=zipfile.ZIP_DEFLATED)
        z.writestr("OEBPS/nav.xhtml", nav, compress_type=zipfile.ZIP_DEFLATED)
        z.writestr("OEBPS/style.css", CSS, compress_type=zipfile.ZIP_DEFLATED)
        for f, t, body in chapters:
            z.writestr(f"OEBPS/{f}", xhtml(t, body), compress_type=zipfile.ZIP_DEFLATED)
    return out


if __name__ == "__main__":
    for arg in sys.argv[1:]:
        print(build(Path(arg)))
