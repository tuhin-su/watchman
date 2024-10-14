sudo mkdir /opt/watchman
sudo mv -v main /opt/watchman/
sudo chmod +x /opt/watchman/main
sudo cp -p watchman.service /etc/systemd/system/watchman.service
sudo cp -p watchman.conf /opt/watchman/main
sudo systemctl daemon-reload
sudo systemctl enable watchman.service --now