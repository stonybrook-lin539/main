#!/usr/bin/evn sh

rsync -av --prune-empty-dirs --include '*/' --include '*.pdf' --exclude '*' build/pdf/sections/ pdf/
