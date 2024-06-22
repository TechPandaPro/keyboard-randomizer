# Keyboard Randomizer

## Overview

A simple Python script that randomly sends mouse and keyboard inputs as you interact with your computer.

There's no practical use for this. Use it at the risk of becoming frustrated. :)

**This script has only been tested on macOS Sonoma. Other platforms _should_ work, but I have not tested it.**

## Usage

### Installation

```bash
git clone https://github.com/TechPandaPro/keyboard-randomizer.git
cd keyboard-randomizer
pip install -r requirements.txt
```

### Permissions

If using macOS, you will have to grant additional permissions to the app running this script (e.g. Terminal). This is because the script needs to be able to read and control inputs.

Toggle the app ON within **both** of the following places.

1. `System Settings > Privacy & Security > Accessibility`
2. `System Settings > Privacy & Security > Input Monitoring`

### Running

```bash
python3 main.py
```
