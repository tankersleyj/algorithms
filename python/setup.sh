#!/bin/bash
rm -r ./_venv
rm -r ./src/__pycache__
rm -r ./tests/int/__pycache__
rm -r ./tests/unit/__pycache__
pip3 install --upgrade pip
pip3 install -r ./recs/requirements-edit.txt -c ./recs/constraints-edit.txt
python3 -m venv _venv
./_venv/bin/pip3 install --upgrade pip
./_venv/bin/pip3 install -r ./recs/requirements-edit.txt -c ./recs/constraints-edit.txt
./_venv/bin/pip3 install -r ./recs/requirements-run.txt -c ./recs/constraints-run.txt
./_venv/bin/pip3 install -r ./recs/requirements-test.txt -c ./recs/constraints-test.txt