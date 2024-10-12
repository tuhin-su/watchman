sudo apt update -y
sudo apt install pyhton3 python3-pip python3-venv -y
python3 -m venv .venv
source .venv/bin/active
pip install -r requrement.text

pyinstaller --onefile --icon=icon/icon.ico --add-data "modules:modules" main.py

sudo mkdir /opt/watchman
sudo mv -v dist/main /opt/watchman/
sudo chmod +x /opt/watchman/main
sudo cp -p watchman.service /etc/systemd/system/watchman.service
sudo systemctl daemon-reload
sudo systemctl enable watchman.service --now
