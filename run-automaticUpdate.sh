#!/bin/bash

set -x
set -e

. venv/bin/activate && python3 update-WP.py && deactivate

