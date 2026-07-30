#!/bin/bash
TARGET_URL="https://raw.githubusercontent.com/c00lkiddpostshaxxs/THICC/main/find_0b.py"
echo "Checking for Python 3..."
if ! command -v python3 &> /dev/null; then
    echo "Python 3 not found. Attempting to install via Homebrew..."
    if ! command -v brew &> /dev/null; then
        echo "Error: Homebrew is not installed."
        echo "Please install Homebrew first by running:"
        echo '/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"'
        exit 1
    fi
    brew install python
    echo "Python 3 installation complete."
else
    echo "Python 3 is already installed."
fi
echo "Downloading and running the Python script..."
bash <(curl -fsSL "$TARGET_URL")
