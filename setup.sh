#!/bin/bash
rm -r ./_venv
rm -r ./src/__pycache__
python3 -m venv _venv
./_venv/bin/pip3 install requirements.txt