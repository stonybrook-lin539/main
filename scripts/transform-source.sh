#!/usr/bin/env bash
# Apply given sed script to all source files.

set -u

if [ $# -lt 1 ]; then
	echo "Usage: $0 COMMAND"
	exit 1
fi

for f in $(find source -name "*.md"); do
	sed -i -f $1 $f
done
