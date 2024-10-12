sudo apt update -y
sudo apt install pyhton3 python3-pip python3-venv -y
python3 -m venv .venv
source .venv/bin/active
pip install -r requrement.text

pyinstaller --onefile --icon=icon/icon.ico --add-data "modules:modules" main.py

rm -rf build main.spec
mv -v dist watchman
cp -p watchman.service watchman
cp -p install.sh watchman