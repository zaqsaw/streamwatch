#!/usr/bin/env bash

mkdir -p $HOME/venv/streamdl_env
python3 -m venv $HOME/venv/streamdl_env
source $HOME/venv/streamdl_env/bin/activate
python3 -m pip install wheel
python3 -m pip install streamlink
python3 -m pip install ffmpeg-python
python3 -m pip install mypy
