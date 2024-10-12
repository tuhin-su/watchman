import os
from datetime import datetime

def log(text: str):
    # Define the directory path
    log_dir = '/var/log/watchman/'
    # Check if the directory exists, if not, create it
    if not os.path.exists(log_dir):
        os.makedirs(log_dir, exist_ok=True)

    # Get the current date and time
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # Define the log file path with the current date
    log_file = os.path.join(log_dir, f'{datetime.now().strftime("%Y-%m-%d")}_watchman.log')

    # Write the log entry
    with open(log_file, 'a') as file:
        file.write(f'{current_time}: {text}\n')
