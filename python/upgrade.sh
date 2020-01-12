#!/bin/bash
pip3 install --upgrade pip
pip3 install -r ./recs/requirements-edit.txt -U
./_venv/bin/pip3 install --upgrade pip
./_venv/bin/pip3 install -r ./recs/requirements-run.txt -U
./_venv/bin/pip3 install -r ./recs/requirements-test.txt -U