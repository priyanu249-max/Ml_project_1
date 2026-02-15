import logging
import os
from datetime import datetime

# Create logs folder path
logs_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir, exist_ok=True)

# Create log file name
log_file = f"{datetime.now().strftime('%m_%d_%Y')}.log"
log_path = os.path.join(logs_dir, log_file)

# Configure logging
logging.basicConfig(
    filename=log_path,
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
