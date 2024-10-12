import os

def log(text: str):
    # Define the directory path
    log_dir = '/var/logs/watchman/'
    # Check if the directory exists, if not, create it
    if not os.path.exists(log_dir):
        os.makedirs(log_dir, exist_ok=True)
    
    # Define the log file path with the current date
    log_file = os.path.join(log_dir, f'$(date +%Y-%m-%d)_watchman.log')
    
    # Write the log entry
    os.system(f'echo "{text}" >> {log_file}')
