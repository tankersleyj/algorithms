#!/bin/bash
# reference: http://pycodestyle.pycqa.org/en/latest/intro.html
echo
echo "-> pycodestyle"
if [ "$1" == '-h' -o "$1" == '--help' ]; then
    echo "options: -h, --help, -v, --verbose"
elif [ "$1" == '-v' -o "$1" == '--verbose' ]; then
    pycodestyle src --show-source --show-pep8
else
    pycodestyle src --format=default
fi