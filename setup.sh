#!/bin/bash
rm -rf env
python3 -m venv env
. env/bin/activate
pip install --upgrade pip
pip3 install Shapely
pip3 install matplotlib
pip3 install pytest