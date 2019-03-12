#!/bin/bash

set -e
CODE_DIR="/analysis/inputs/public/source-code"

whitespace () {
    num_ws=$(gawk -v RS='[[:space:]]' 'END{print NR}' "$1")
    total=$(wc -c $1 | cut -d ' ' -f 1)
    path=$(echo $1 | cut -c 3-)
    echo -e "{ \n\
    \"check_id\": \"whitespace\", \n\
    \"path\": \"${path}\", \n\
    \"extra\": { \n\
      \"whitespace\": ${num_ws}, \n\
      \"total\": ${total} \n\
      } \n\
    }"
}

export -f whitespace

cd ${CODE_DIR}

find . -name '*.js' | \
  xargs -n 1 -I {} bash -c 'whitespace "$@"' _ {} | \
  jq -s '{results: .}' | \
  tee /analysis/output/output.json