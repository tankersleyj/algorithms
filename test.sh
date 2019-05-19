#!/bin/bash
if [ $# -eq 0 -o "$1" == '-h' -o "$1" == '--help' ]; then
  echo "Required: <folder> [<pattern>]"
  echo "Examples:"
  echo "  ./test.sh tests"
  echo "  ./test.sh tests/unit"
  echo "  ./test.sh tests/unit *sort*"
elif [ $# -eq 1 ]; then
  ./_venv/bin/python3 -m unittest discover -s "./$1"
else
  ./_venv/bin/python3 -m unittest discover -s "./$1" -p "$2"
fi
