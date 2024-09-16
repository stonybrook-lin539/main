#!/usr/bin/env sh

# copy pdf book
rsync -av --delete build/pdf/full-book.pdf output/

# copy pdf sections
rsync -av --prune-empty-dirs --delete --include '*/' --include '*.pdf' --exclude '*' build/pdf/sections/ output/pdf_sections/

# run html and copy output, except solutions
doit html_website
rsync -av --prune-empty-dirs --delete --exclude 'solutions' build/html/ output/html

# and push to github
if [ "$1" = "remote" ]; then
    git add output
    git commit -m "recompile pdf & html"
    git push origin master
    # # git subtree push --prefix output/html origin gh-pages
    git push origin `git subtree split --prefix output/html master`:gh-pages --force
fi
