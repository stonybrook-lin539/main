#!/usr/bin/env sh

rsync -av --prune-empty-dirs --delete --include '*/' --include '*.pdf' --exclude '*' build/pdf/sections/ output/pdf/

rsync -av --prune-empty-dirs --delete build/html/ output/html

git add output
git commit -m "recompile pdf & html"
git push origin master
# git subtree push --prefix output/html origin gh-pages
git push origin `git subtree split --prefix output/html master`:gh-pages --force
