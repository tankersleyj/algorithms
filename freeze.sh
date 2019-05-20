#!/bin/bash
pip3 freeze -r ./recs/constraints-edit.txt > ./recs/requirements-edit.txt
./_venv/bin/pip3 freeze -r ./recs/constraints-run.txt > ./recs/requirements-run.txt
./_venv/bin/pip3 freeze -r ./recs/constraints-test.txt > ./recs/requirements-test.txt