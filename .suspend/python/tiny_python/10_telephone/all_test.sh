#!/usr/bin/env bash

set -eu -o pipefail

PRG="telephone.py"
for FILE in solution*.py; do
    echo "==> ${FILE} <==" 
    cp "$FILE" "$PRG"
    make test
done

echo "Done."
