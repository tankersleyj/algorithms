#!/bin/bash
if [ $# -gt 0 ]; then
  if echo "$1" | grep -q ".py"; then
    echo "Test file(s): $@"
    ./_venv/bin/python3 -m unittest $@
  else
    echo "Test folder: $1"
    ./_venv/bin/python3 -m unittest discover -s $1
  fi
else
  echo "Help: Select folder or file do you want to test"
  echo "Example: 'tests' or 'test/test_timer.py'"
fi
