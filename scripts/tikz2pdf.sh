#!/usr/bin/env bash
# Convert tikz to standalone file to SVG
# Based on the "tikztosvg" utility in TeXLive, but does not attempt
#   to modify source file
set -u

if [ $# -lt 2 ]; then
	echo "USAGE: $0 INFILE OUTFILE"
    exit 1
fi

if ! [ -x "$(command -v pdflatex)" ]
then
  error "pdflatex could not be found"
fi

if ! [ -x "$(command -v pdf2svg)" ]
then
  error "pdf2svg could not be found"
fi

infile="$1"
outfile="$2"
tempdir="$(mktemp -td tikz2svg-XXXXX)"
pdffile="${tempdir}/$(basename ${infile%%.*}).pdf"

pdflatex -interaction=nonstopmode -halt-on-error -output-dir "$tempdir" "$infile"

S=$?
if [ $S -ne 0 ]
then
    rm "$tempdir" -rf
    echo "pdflatex exited with code $S"
    exit $S
fi

mv "$pdffile" "$outfile"

rm "$tempdir" -rf
