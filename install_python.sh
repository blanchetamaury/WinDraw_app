#!/bin/bash

pip install -r requirements.txt

pyinstaller \
  --onefile \
  --add-data "assets:assets" \
  --hidden-import PIL._tkinter_finder \
  --name WinDraw \
  draw_window.py

cp dist/Windraw .