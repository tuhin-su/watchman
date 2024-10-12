sudo apt install pyhton3 python3-pip python3-venv
python3 -m venv .venv
source .venv/bin/active
pip install -r requrement.text

pyinstaller --onefile --icon=path/to/your/icon.ico --add-data "modules:modules" main.py
