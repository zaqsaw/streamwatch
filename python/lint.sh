#!/usr/bin/env bash

source $HOME/venv/streamdl_env/bin/activate
mypy download_live_stream.py --ignore-missing-imports --disallow-untyped-defs --disallow-untyped-calls --disallow-incomplete-defs --disallow-untyped-decorators
