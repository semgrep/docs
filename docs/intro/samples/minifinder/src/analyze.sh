#!/bin/bash

set -e
CODE_DIR="/analysis/inputs/public/source-code"

cd ${CODE_DIR}

find . -type f -name '*.js' -print0 | xargs -0 python3 /analyzer/whitespace.py
