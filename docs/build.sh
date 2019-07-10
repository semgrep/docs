#!/bin/bash

set -e
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

cd ${DIR}/intro/samples/minifinder
r2c --debug test 
cd ${DIR}/intro/samples/minifinder2
r2c --debug test 
cd ${DIR}/intro/samples/typed-ast-rules-example
r2c --debug test 

echo 'all tests have succeeded!'