
# Do not run this file "day8.py" 💀❌💀❌💀 



#============😎============😎============😎============😎============😎
# Example 1

import subprocess

result = subprocess.run(["ls", "-l"], capture_output=True, text=True)
print(result.stdout)





#===========================😎============😎============😎============😎============😎
# Example 2

import os
import shutil

# File paths
source_file = "new.txt"  # Change this to your actual source file
destination_folder = "new_folder/"
new_file = "new.txt"


def create_file(file_path, content="Hello, this is a test file, with 🍉!"):
    """Creates a new file with sample content."""
    with open(file_path, "w") as file:
        file.write(content)
    print(f"File created: {file_path}")

def delete_file(file_path):
    """Deletes the specified file if it exists."""
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"File deleted: {file_path}")
    else:
        print("File not found!")

def copy_file(source, destination):
    """Copies a file to a destination."""
    if os.path.exists(source):
        shutil.copy(source, destination)
        print(f"File copied from {source} to {destination}")
    else:
        print("Source file not found!")

def move_file(source, destination):
    """Moves a file to a new location."""
    if os.path.exists(source):
        shutil.move(source, destination)
        print(f"File moved from {source} to {destination}")
    else:
        print("Source file not found!")

# Example Usage
if __name__ == "__main__":
    # Create a new file
    # create_file(new_file)

    # # Copy the file
    # copy_file(source_file, destination_folder)

    # # Move the file
    # move_file(source_file, destination_folder)

    # # Delete the copied file
    # delete_file(source_file)


#==😎============😎=================😎============😎=================😎============

#Example 3


import os
import psutil
from datetime import datetime

# Configuration
THRESHOLD_PERCENTAGE = 20  # Alert if disk usage exceeds 80%
DIRECTORY_TO_CHECK = "/"  # Root directory
LOG_FILE = "/var/log/disk_usage.log"  # Log file location

def check_disk_usage():
    """Check the disk usage of the specified directory."""
    usage = psutil.disk_usage(DIRECTORY_TO_CHECK)
    return usage.percent

def log_alert(usage):
    """Log disk usage alert to a file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"[{timestamp}] ALERT: Disk usage exceeded {THRESHOLD_PERCENTAGE}% - Current: {usage}%\n"

    with open(LOG_FILE, "a") as log_file:
        log_file.write(log_message)

    print("Alert logged:", log_message.strip())

if __name__ == "__main__":
    usage = check_disk_usage()
    print(f"Current Disk Usage: {usage}%")

    if usage > THRESHOLD_PERCENTAGE:
        print("Disk usage exceeded threshold! Logging alert...")
        log_alert(usage)
    else:
        print("Disk usage is within safe limits.")
