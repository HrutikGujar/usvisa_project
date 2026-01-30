import logging
import os
from datetime import datetime
#from from_root import from_root

LOG_DIR = "logs"
LOG_FILE = f"{datetime.now().strftime('%m_%d_%y_%H_%M_%S')}.log"

# Hardcode the project root to ensure it's on D drive
project_root = r"d:\PROJECT\mlops_visa\usvisa_project"
log_dir_path = os.path.join(project_root, LOG_DIR)
#print(f"Log directory path: {log_dir_path}")  # Debug: Check the path
os.makedirs(log_dir_path, exist_ok=True)

log_file_path = os.path.join(log_dir_path, LOG_FILE)
#print(f"Log file path: {log_file_path}")  # Debug: Check the full file path

logging.basicConfig(
    filename=log_file_path,
    format="[%(asctime)s] %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)

# Test log to ensure file is created
logging.debug("Logger initialized successfully.")
