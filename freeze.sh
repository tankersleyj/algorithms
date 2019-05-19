#!/bin/bash MIT (c) jtankersley 2019-05-18
rm -r ./_venv
rm -r ./src/__pycache__
python3 -m venv _venv
./_venv/bin/pip3 install --upgrade pip
./_venv/bin/pip3 install constraints.txt
./_venv/bin/pip3 freeze -r constraints.txt > requirements.txt