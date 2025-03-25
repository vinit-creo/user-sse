#!/bin/bash
# shellcheck disable=SC2068

chmod +x ./install_script.sh


python -m venv sse && . sse/bin/activate && pip install -r requirement.txt