#!/bin/bash

# Define variables
INSTALL_DIR="/opt/RobertAI-main"
ZIP_FILE="/usr/bin/AstraOS-assets/main.zip"
DESKTOP_FILE="robert.desktop"
EXECUTABLE="main_script.py"

# Ensure script is run as root
if [ "$(id -u)" != "0" ]; then
    echo "This script must be run as root" 1>&2
    exit 1
fi

# Extract files
mkdir -p $INSTALL_DIR
unzip -o $ZIP_FILE -d $INSTALL_DIR || { echo "Extraction failed"; exit 1; }

# Create desktop shortcut
echo "[Desktop Entry]
Version=1.0
Type=Application
Name=Robert
Comment=A companion that will help you with whatever you want.
Exec=python3 $INSTALL_DIR/$EXECUTABLE
Icon=$INSTALL_DIR/icon.png
Terminal=false
Categories=Utility;" > /usr/share/applications/$DESKTOP_FILE

# Set permissions
chmod +x $INSTALL_DIR/$EXECUTABLE

echo "Installation completed successfully"
