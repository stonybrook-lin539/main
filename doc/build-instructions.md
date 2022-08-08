# Build instructions

## Requirements

- Python >= 3.10
- Doit >= 0.34
- Pandoc >= 2.9
- TeXLive 2022
- bash, sed

Everything is tested only on Ubuntu 22.04. The build script may work with older software, but has not been tested.

A script that checks for required software and LaTeX packages has been provided in the `scripts` directory. Run `scripts/check-deps.sh` with argument `list` to list all requirements, and `check` to check if they are installed.

## Software installation

Python and Pandoc are from the Ubuntu software repository. Python is installed by default on most distros. Pandoc may be installed using `apt install pandoc`.

Doit is installed via pip: `pip install pandoc`. If pip is not already installed, install it using `apt install python3-pip`.

Installation of TeXLive is beyond the scope of this document. The simplest option is to do a full install from the Ubuntu repos: `apt install texlive-full`.

Bash and sed are almost certainly already installed on your system.

## How to build

The Python program "Doit" is used to convert the source files into PDF and HTML form.

- To build everything, simply run `doit` from the project root.
- To selectively build one or more formats, run `doit TASK`.
- To see all available tasks, run `doit list`.

A makefile for GNU Make is also available, but is extremely outdated. For now, use Doit.
