#!/bin/bash

set -e
AST_DIR="/analysis/inputs/r2c/typed-ast"

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
node $DIR/dist/src/index.js $AST_DIR >/analysis/output/output.json
