#!/bin/bash
if [ $# -gt 0 ]; then
  if echo "$1" | grep -q ".py"; then
    echo "Test file(s): $@"
    ./_venv/bin/python3 -m unittest $@
  else
    echo "Test folder: ./$1"
    ./_venv/bin/python3 -m unittest discover -s "./$1"
  fi
else
  echo "Help: Test <folder> or <file(s)>"
  echo "Examples:"
  echo "  ./test.sh tests"
  echo "  ./test.sh tests/test_sort.py"
  echo "  ./test.sh */*_sort.py */*_timer.py"
fi
