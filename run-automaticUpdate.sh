#!/bin/bash

set -x
set -e

. venv/bin/activate && python3 append-to-bash.py && deactivate

