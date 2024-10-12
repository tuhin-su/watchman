import os

def log(text:str):
    os.system(f'echo "{text}" >> /var/logs/watchman/$(date +%Y-%m-%d)_watchman.log')