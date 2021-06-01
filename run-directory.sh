#!/bin/bash

set -x
set -e

. venv/bin/activate

python3 directory.py

deactivate

