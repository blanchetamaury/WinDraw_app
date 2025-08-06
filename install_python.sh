#!/bin/bash

sudo apt update
sudo apt upgrade
sudo apt install python3
sudo apt install python3-tk
sudo apt install python3-venv

python3 -m venv windraw

source windraw/bin/activate

pip install -r requirements.txt

pyinstaller \
  --onefile \
  --add-data "assets:assets" \
  --hidden-import PIL._tkinter_finder \
  --name WinDraw \
  draw_window.py

cp dist/WinDraw .