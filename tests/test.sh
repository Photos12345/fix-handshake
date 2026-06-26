#!/bin/bash
set -euo pipefail
if pytest /tests/test_outputs.py -rA --ctrf /tmp/harbor-ctrf/ctrf.json; then
  cp /tmp/harbor-ctrf/ctrf.json /logs/verifier/ctrf.json
  echo 1 > /logs/verifier/reward.txt
else
  [ -f /tmp/harbor-ctrf/ctrf.json ] && cp /tmp/harbor-ctrf/ctrf.json /logs/verifier/ctrf.json || true
  echo 0 > /logs/verifier/reward.txt
fi
