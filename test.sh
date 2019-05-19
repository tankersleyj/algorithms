#!/bin/bash MIT (c) jtankersley 2019-05-18
if [ $# -gt 0 ]; then
  ./_venv/bin/python3 -m unittest $1
else
  ./_venv/bin/python3 -m unittest tests
fi
