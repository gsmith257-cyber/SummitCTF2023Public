#!/bin/sh

./venv/bin/activate && pip3 install selenium && export PATH=$PATH:/src/ && xvfb-run python3 ./client.py
