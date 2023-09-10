#!/bin/bash
if [ $# -eq 0 -o "$1" == '-h' -o "$1" == '--help' ]; then
  echo "Required: <folder> [<pattern>]"
  echo "Examples:"
  echo "  ./test.sh tests"
  echo "  ./test.sh tests/unit *sort*"
elif [ $# -eq 1 ]; then
  .conda/python -m unittest discover -s "./$1"
else
  .conda/python -m unittest discover -s "./$1" -p "$2"
fi
