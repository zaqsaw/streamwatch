#!/usr/bin/env bash

source $HOME/venv/streamwatcher_env/bin/activate
mypy . --ignore-missing-imports --disallow-untyped-defs --disallow-untyped-calls --disallow-incomplete-defs --disallow-untyped-decorators
