#!/bin/bash

pip install pyinstaller

pyinstaller \
  --onefile \
  --add-data "assets:assets" \
  --hidden-import PIL._tkinter_finder \
  --name WinDraw \
  draw_window.py

cp dist/Windraw .

DESKTOP_INSTALL_PATH="$HOME/.local/share/applications"
ICON_INSTALL_PATH="$HOME/.local/share/icons/hicolor/256x256/apps"

APP_NAME="WinDraw"
EXEC_PATH="$(pwd)/$APP_NAME"
ICON_PATH="icon.png"
DESKTOP_FILE="$APP_NAME.desktop"

mkdir -p "$ICON_INSTALL_PATH"
mkdir -p "$DESKTOP_INSTALL_PATH"

cp "$ICON_PATH" "$ICON_INSTALL_PATH/$APP_NAME.png"

echo "[Desktop Entry]" > "$DESKTOP_FILE"
echo "Version=1.0" >> "$DESKTOP_FILE"
echo "Name=$APP_NAME" >> "$DESKTOP_FILE"
echo "Comment=Application for drawing to the screen" >> "$DESKTOP_FILE"
echo "Exec=$EXEC_PATH" >> "$DESKTOP_FILE"
echo "Path=$(pwd)" >> "$DESKTOP_FILE"
echo "Icon=$APP_NAME" >> "$DESKTOP_FILE"
echo "Terminal=false" >> "$DESKTOP_FILE"
echo "Type=Application" >> "$DESKTOP_FILE"
echo "Categories=Utility;" >> "$DESKTOP_FILE"

cp "$DESKTOP_FILE" "$DESKTOP_INSTALL_PATH/"
chmod +x "$DESKTOP_INSTALL_PATH/$DESKTOP_FILE"

xdg-icon-resource forceupdate --size 256
