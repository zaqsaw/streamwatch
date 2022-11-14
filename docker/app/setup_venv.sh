#!/usr/bin/env bash

mkdir -p $HOME/venv/streamwatcher_env
python3 -m venv $HOME/venv/streamwatcher_env
source $HOME/venv/streamwatcher_env/bin/activate
python3 -m pip install wheel
python3 -m pip install streamlink
python3 -m pip install pytz
python3 -m pip install types-pytz
python3 -m pip install mypy
