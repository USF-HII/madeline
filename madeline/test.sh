#!/usr/bin/env bash

cmd() {
  echo 1>&2
  echo "cmd> "$@"" 1>&2
  "$@"
}

test_submit() {
  cmd curl -s -X POST --data @tests/data/request-with-tsv.json http://app:5000/submit

    #--custom-icon-colors 'ALS=red,PLS=purple,PMA=blue,HSP=green;A=black;FTD=black,Non-FTD=lightgray;A=black'" \
    #--data-urlencode args="--color --nolabeltruncation" \
}

test_version() {
  cmd curl -s http://app:5000/version
}

test_submit

test_version

python client.py
