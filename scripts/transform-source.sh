#!/usr/bin/env sh
set -u

for f in $(find source -name "*.md"); do
	sed -i -f $1 $f
done
