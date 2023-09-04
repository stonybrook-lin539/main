#!/usr/bin/env sh

rsync -av --prune-empty-dirs --delete --include '*/' --include '*.pdf' --exclude '*' build/pdf/sections/ output/pdf/
rsync -av --prune-empty-dirs --delete build/html/ output/html
