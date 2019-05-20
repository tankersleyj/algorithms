#!/bin/bash
rm -r ./_venv
rm -r ./src/__pycache__
rm -r ./tests/int/__pycache__
rm -r ./tests/unit/__pycache__
python3 -m venv _venv
./_venv/bin/pip3 install --upgrade pip
./_venv/bin/pip3 install -r requirements.txt -c constraints.txt