# to add logging
import logging
import os
from datetime import datetime

def setupLogging():
    # Ensure the logs/ folder exists
    os.makedirs("logs", exist_ok=True)
    curr_date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_file = f"logs/{curr_date}.log"
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%d/%m/%Y %I:%M:%S %p",
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ])