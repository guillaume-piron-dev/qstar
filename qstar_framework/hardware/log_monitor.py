# qstar/hardware/log_monitor.py
import logging
import datetime
import os

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, f"qstar_{datetime.date.today()}.log")

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

logging.basicConfig(
    filename=LOG_FILE,
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO
)

def log_system_event(event: str):
    logging.info(event)

def log_warning(msg: str):
    logging.warning(msg)

def log_error(msg: str):
    logging.error(msg)

if __name__ == "__main__":
    log_system_event("Initialisation du module Q-STAR Hardware Log")
