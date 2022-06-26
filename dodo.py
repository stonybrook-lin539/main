"""
Doit task definition file for LIN 539 course notes.
"""

from pathlib import Path
from itertools import chain
# from doit.tools import title_with_actions

DOIT_CONFIG = {"default_tasks": ["pdf_book", "pdf_chaps", "pdf_sections"],
               "check_file_uptodate": "timestamp"}
# DOIT_CONFIG = {"action_string_formatting": "new"}

# external programs
TIKZ2SVG = "scripts/tikz2svg.sh"
LATEX = "latexmk -pdf -interaction=nonstopmode -halt-on-error"

# custom Pandoc filters
CSTM_BLKS = "filters/custom-blocks.lua"
INCL_FILE = "filters/include-file.lua"
LATEX_TIPA = "filters/latex-tipa.lua"
STRIP_CODE = "filters/remove_code.lua"
EDGEMARKERS = "filters/edgemarkers.lua"

# Pandoc templates and includes
LATEX_TEMPLATE = "templates/latex-custom.tex"
# LATEX_BOOK_TEMPLATE = "templates/full-book.tex"
# LATEX_CH_TEMPLATE = "templates/single-chapter.tex"
MATHCMDS = Path("includes/mathcommands.md")
LATEX_PREAMBLE = Path("includes/preamble.tex")
# YAMLHEADER = Path("includes/format.yaml")
# CSS path must be absolute to load locally
WEBCSS = Path("includes/web-custom.css").resolve()
MATHJAXCALL = Path("includes/include-mathjax.html")

# source files/directories
MD_EXTS = (".mdown", ".md")
TIKZ_EXTS = (".tikz", ".forest")
SRCDIR = Path("source")
SRC_MD = sorted(f for f in SRCDIR.glob('**/*') if f.suffix in MD_EXTS
                and "old" not in f.parts
                and "solutions" not in f.parts)
SRC_TEX = sorted(f for f in SRCDIR.glob('**/*') if f.suffix == ".tex")
SRC_TIKZ = sorted(f for f in SRCDIR.glob('**/*') if f.suffix in TIKZ_EXTS)

# source directories
MAIN_CHAPS = [f"main/{ch}" for ch in
              ["01_intro", "02_n-grams", "03_universals", "04_representations",
               "05_automata"]]
BG_CHAPS = [f"background/{ch}" for ch in
            ["algebra", "functions", "general", "graphs", "logic", "multisets",
             "posets", "relations", "sets", "strings", "tuples"]]
ALL_CHAPS = MAIN_CHAPS + BG_CHAPS
# ALL_CHAPS += ["solutions/01_intro", "solutions/02_n-grams",
#                "solutions/03_universals", "solutions/04_representations",
#                "solutions/05_automata"]
# ALL_CHAPS += [f"solutions/background/{subch}" for subch in
#                ["functions", "general", "graphs", "logic", "multisets",
#                 "posets", "relations", "sets", "strings", "tuples"]]
# MAIN_CH_DIRS = sorted(d for d in Path("source/main").iterdir() if d.is_dir())
# BG_CH_DIRS = sorted(d for d in Path("source/background").iterdir() if d.is_dir())
# ALL_CH_DIRS = MAIN_CH_DIRS + BG_CH_DIRS

# output files/directories
BUILDDIR = Path("build")
IMGDIR = BUILDDIR / "images"
TEXDIR = BUILDDIR / "latex"
PDFDIR = BUILDDIR / "pdf"
HTMLDIR = BUILDDIR / "html"
MODCMDS = BUILDDIR / "mathcommands-preproc.md"

MD_BOOK = SRCDIR / "full-book.md"
TEX_BOOK = TEXDIR / "full-book.tex"
PDF_BOOK = PDFDIR / "full-book.pdf"

# Pandoc shared dependencies
LATEX_DEPS = [CSTM_BLKS, INCL_FILE, LATEX_TIPA, EDGEMARKERS,
              LATEX_TEMPLATE, LATEX_PREAMBLE, MODCMDS]
HTML_DEPS = [CSTM_BLKS, INCL_FILE,
             WEBCSS, MATHJAXCALL, MODCMDS]

# Pandoc shared options
PANDOC_OPTS = (
    "-f markdown-implicit_figures"
    f" --metadata-file={SRCDIR}/metadata.yaml"
    # " -V showanswers"
    f" -L {CSTM_BLKS}"
    f" -L {INCL_FILE}"
)

LATEX_OPTS = (
    f"--template {LATEX_TEMPLATE}"
    f" -H {LATEX_PREAMBLE}"
    f" -H {MODCMDS}"
    f" -L {LATEX_TIPA}"
    f" -L {EDGEMARKERS}"
)

HTML_OPTS = (
    f"--shift-heading-level-by=1 -c {WEBCSS}"
    f" --mathjax -Vmath='' -H {MATHJAXCALL}"  # see task def for details
    f" {MODCMDS}"
)


#
# Tasks to build just part of the book for faster testing
#

def task_test_chapter():
    """Compile just one chapter to PDF."""
    chname = "02_n-grams"
    srcsubdir = SRCDIR / "main" / chname
    infiles = sorted(str(f) for f in srcsubdir.glob("*.md"))
    outfile = f"{PDFDIR}/test/{chname}.pdf"
    cmd = (
        f"TEXINPUTS=.:{srcsubdir}:"
        f" pandoc -t pdf {PANDOC_OPTS} {LATEX_OPTS}"
        " --toc --toc-depth 1"
        " -M singlechapter"
        f" --metadata-file={srcsubdir}/metadata.yaml"
        " --verbose"
        f" {' '.join(infiles)} -o {outfile}"
    )
    return {
        "targets": [outfile],
        "file_dep": [*infiles, *LATEX_DEPS],
        "actions": [f"mkdir -p $(dirname {outfile})", cmd],
        "clean": True}


def task_test_section():
    """Compile just one section to PDF."""
    chname = "02_n-grams"
    secname = "00_ngrams"
    srcsubdir = SRCDIR / "main" / chname
    infile = f"{srcsubdir}/{secname}.md"
    outfile = f"{PDFDIR}/test/{chname}/{secname}.pdf"
    cmd = (
        f"TEXINPUTS=.:{srcsubdir}:"
        f" pandoc -t pdf {PANDOC_OPTS} {LATEX_OPTS}"
        " -M singlesection"
        " --shift-heading-level-by=-1"
        f" --metadata-file={srcsubdir}/metadata.yaml"
        " --verbose"
        f" {infile} -o {outfile}"
    )
    return {
        "targets": [outfile],
        "file_dep": [infile, *LATEX_DEPS],
        "actions": [f"mkdir -p $(dirname {outfile})", cmd],
        "clean": True}


#
# Pre-processing
#

def task_mathcommands():
    """
    Preprocess custom command file for PDF (LaTeX) and HTML conversion.

    At present, simply removes surrounding $ signs, which are needed
    for Jupyter only, and commented lines, which interfere with non-LaTeX
    build paths.
    """
    return {
        "targets": [MODCMDS],
        "file_dep": [MATHCMDS],
        "actions": [
            f"mkdir -p $(dirname {MODCMDS})",
            ("sed -e 's/\\(^\\$\\|\\$$\\)//g' -e '/^%%/d'"
             f" {MATHCMDS} > {MODCMDS}")],
            "clean": True}


#
# PDF/LaTeX build path -- full book
#

def task_latex_book():
    """
    Build entire book as LaTeX using Pandoc.
    """
    srcsubdirs = [SRCDIR / ch for ch in ALL_CHAPS]
    infiles = [str(f) for f in chain.from_iterable(
               sorted(subdir.glob("*")) for subdir in srcsubdirs)
               if f.suffix in (".tex", ".md")]
    outfile = TEX_BOOK
    cmd = (
        f" pandoc -t latex {PANDOC_OPTS} {LATEX_OPTS}"
        # f" --template {LATEX_TEMPLATE}"
        " --toc --toc-depth 1"
        f" {' '.join(infiles)} -o {outfile}"
    )
    return {
        "targets": [outfile],
        "file_dep": [*infiles, *LATEX_DEPS],
        "actions": [f"mkdir -p {outfile.parent}", cmd],
        "clean": True}


def task_pdf_book():
    """
    Compile PDF book from LaTeX generated by Pandoc.
    """
    srcsubdirs = [SRCDIR / ch for ch in ALL_CHAPS]
    infile = TEX_BOOK
    outfile = PDF_BOOK
    cmd = (
        f"TEXINPUTS=.:{':'.join(str(sd) for sd in srcsubdirs)}:"
        f" {LATEX} -output-directory={outfile.parent} {infile}"
    )
    return {
        "targets": [outfile],
        "file_dep": [infile],
        "actions": [f"mkdir -p {outfile.parent}", cmd],
        "clean": True}


#
# PDF/LaTeX build path -- standalone chapters
#

def task_latex_chaps():
    """
    Build LaTeX standalone chapters with Pandoc.
    """
    for ch in ALL_CHAPS:
        srcsubdir = SRCDIR / ch
        infiles = [str(f)
                   for f in sorted(srcsubdir.glob("*.md"))]
        outfile = TEXDIR / f"chapters/{ch}.tex"
        cmd = (
            f"pandoc -t latex {PANDOC_OPTS} {LATEX_OPTS}"
            " -M singlechapter"
            f" --metadata-file={srcsubdir}/metadata.yaml"
            f" {' '.join(infiles)} -o {outfile}"
        )
        yield {
            "name": outfile,
            "targets": [outfile],
            "file_dep": [*infiles, *LATEX_DEPS],
            "actions": [f"mkdir -p {outfile.parent}", cmd],
            "clean": True}


def task_pdf_chaps(test=True):
    """
    Build PDF chapters from LaTeX generated by Pandoc.
    """
    for ch in ALL_CHAPS:
        srcsubdir = SRCDIR / ch
        infile = f"{TEXDIR}/chapters/{ch}.tex"
        outfile = PDFDIR / f"chapters/{ch}.pdf"
        cmd = (
            f"TEXINPUTS=.:{srcsubdir}:"
            f" {LATEX} -output-directory={outfile.parent} {infile}"
        )
        yield {
            "name": outfile,
            "targets": [outfile],
            "file_dep": [infile],
            "actions": [f"mkdir -p {outfile.parent}", cmd],
            "clean": True}


#
# PDF/LaTeX build path -- individual units
#

def task_latex_sections():
    """
    Build LaTeX standalone sections with Pandoc.
    """
    for infile in SRC_MD:
        outfile = TEXDIR / "sections" / infile.relative_to(SRCDIR).with_suffix(".tex")
        cmd = (
            f"pandoc -s -t latex {PANDOC_OPTS} {LATEX_OPTS}"
            " -M singlesection"
            " --shift-heading-level-by=-1"
            f" {infile} -o {outfile}"
        )
        yield {
            "name": outfile,
            "targets": [outfile],
            "file_dep": [infile, *LATEX_DEPS],
            "actions": [f"mkdir -p {outfile.parent}", cmd],
            "clean": True}


def task_pdf_sections():
    """
    Build PDF sections from LaTeX generated by Pandoc.
    """
    for srcfile in SRC_MD:
        srcsubdir = srcfile.parent
        infile = TEXDIR / "sections" / srcfile.relative_to(SRCDIR).with_suffix(".tex")
        outfile = PDFDIR / infile.relative_to(TEXDIR).with_suffix(".pdf")
        cmd = (
            f"TEXINPUTS=.:{srcsubdir}:"
            f" {LATEX} -output-directory={outfile.parent} {infile}"
        )
        yield {
            "name": outfile,
            "targets": [outfile],
            "file_dep": [infile, *LATEX_DEPS],
            "actions": [f"mkdir -p {outfile.parent}", cmd],
            "clean": True}


#
# HTML build path
#

def task_html_chaps():
    """
    Build HTML chapters using Pandoc.

    MODCMDS is inserted in the HTML body so that Pandoc will correctly add
    MathJax delimiters (it will not change included headers).

    Problem: the --mathjax command performs preprocessing, then inserts the
    MathJax script *only if* LaTeX math is detected. This means that in a file
    with no math, the custom commands that we insert will appear as raw text.
    The author of Pandoc has refused to change this. As a workaround, we
    use -Vmath='' to manually clear the internal variable where Pandoc records
    whether math was detected, and insert the script ourselves.
    """
    for ch in ALL_CHAPS:
        infiles = sorted(str(f)
                         for f in Path(f"{SRCDIR}/{ch}").glob("*.md"))
        incl_images = sorted(HTMLDIR / img.relative_to(SRCDIR).with_suffix(".svg")
                             for img in SRC_TIKZ)
        outfile = Path(f"{HTMLDIR}/{ch}/index.html")
        cmd = (
            f"pandoc -t html {PANDOC_OPTS} {HTML_OPTS}"
            f" --metadata title={ch}"
            f" {' '.join(infiles)} -o {outfile}"
        )
        yield {
            "name": outfile,
            "targets": [outfile],
            "file_dep": [*infiles, *incl_images, *HTML_DEPS],
            "actions": [f"mkdir -p $(dirname {outfile})",
                        cmd],
            "clean": True}


def task_html_images():
    """
    Copy pre-converted SVG images to proper directory.
    """
    for img in SRC_TIKZ:
        src = IMGDIR / img.relative_to(SRCDIR).with_suffix(".svg")
        dest = HTMLDIR / src.relative_to(IMGDIR)
        yield {
            "name": dest,
            "targets": [dest],
            "file_dep": [src],
            "actions": [
                f"mkdir -p $(dirname {dest})",
                f"cp {src} {dest}"],
            "clean": True}


def task_images():
    """
    Convert TikZ diagrams to SVG for HTML inclusion.
    """
    for infile in SRC_TIKZ:
        outfile = IMGDIR / infile.relative_to(SRCDIR).with_suffix(".svg")
        yield {
            "name": outfile,
            "targets": [outfile],
            "file_dep": [infile],
            "actions": [
                f"mkdir -p $(dirname {outfile})",
                f"{TIKZ2SVG} {infile} {outfile}"],
            "clean": True}
