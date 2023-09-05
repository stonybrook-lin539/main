#!/usr/bin/env python3
"""
Code to generate table of contents for HTML web book.
"""

from pathlib import Path
import re
import yaml

SRCDIR = Path("source")

print("<div class=\"site-toc\">")
for part in ("main", "background", "exercises"):
    partdir = SRCDIR / part
    partmeta = partdir / "metadata.yaml"
    with open(partmeta, 'r') as file:
        partmetadata = yaml.load(file, Loader=yaml.BaseLoader)
    parttitle = partmetadata["part-title"]
    print(f"<h2 class=\"toc-part\">{parttitle}</h2>")
    for chdir in sorted(p for p in partdir.glob("*") if p.is_dir()):
        chmeta = chdir / "metadata.yaml"
        with open(chmeta, 'r') as file:
            chmetadata = yaml.load(file, Loader=yaml.BaseLoader)
        chtitle = chmetadata["chapter-title"]
        print(f"<h3 class=\"toc-ch\">{chtitle}</h3>")
        for mdfile in sorted(p for p in chdir.glob("*") if p.suffix == ".md"):
            htmlfile = mdfile.relative_to(SRCDIR).with_suffix(".html")
            with open(mdfile) as f:
                for line in f:
                    # match = re.match(r"title:\s*(.*)", line)
                    match = re.match(r"^#\s(.*)", line)
                    if match:
                        print(f"<h4 class=\"toc-sec\">"
                              f"<a href='{htmlfile}'>"
                              f"{match[1]}"
                              f"</a></h4>")
                        break
print("</div>")
