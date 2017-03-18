#!/usr/bin/env bash

cmd() {
  echo 1>&2
  echo "cmd> "$@"" 1>&2
  "$@"
}

jq_filter() {
  jq '.. |= (if type == "string" then .[0:102] else . end)'
}

test_submit() {
  cmd curl -s -X POST --data @tests/data/request-with-tsv.json http://app:5000/submit | jq_filter
}

test_submit_bad() {
  cmd curl -s -X POST --data @tests/data/bad-request-with-xml.json http://app:5000/submit | jq_filter
}

test_version() {
  cmd curl -s http://app:5000/version
}

echo 1>&2
echo "running python client.py" 1>&2

python client.py

test_submit

test_submit_bad

test_version

