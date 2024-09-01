import logging
from pathlib import Path
from datetime import datetime
from django.conf import settings


# LOGGER
# ------
def logger_config(log_file_path: Path):

    """
    Configure the logger to use the specified log file.

    Args:
        log_file_path (Path): The path to the log file.

    Returns: None
    """

    if logger.hasHandlers():
        logger.handlers.clear()
    file_handler = logging.FileHandler(log_file_path, mode='a')
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S'))
    logger.addHandler(file_handler)
    logger.setLevel(logging.INFO)

logger = logging.getLogger('submit_history')

def logger_update(input_text) -> None:
    
    """
    Update the log file "submit_history" with a new entry,
    containing the input text and a timestamp.

    Args:
        input_text (str): The text to be added to the log file.

    Returns: None
    """

    log_file_path = Path(settings.LOG_SUBMIT_HISTORY)

    # Ensure the directory exists and create the log file if it doesn't exist
    log_file_path.parent.mkdir(parents=True, exist_ok=True)
    if not log_file_path.exists():
        log_file_path.touch()
        # Reconfigure the logger to use the new log file
        logger_config(log_file_path)

    # Log the new entry
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    logger.info(f'{timestamp} - {input_text}')

def logger_read() -> list:
    
    """
    Read the log file "submit_history" and return its content
    as a list. If the log file doesn't exist, it creates the file
    and then returns an empty list.

    Args: None

    Returns:
        list: The content of the log file.
    """
    
    history = []
    log_file_path = Path(settings.LOG_SUBMIT_HISTORY)

    log_file_path.parent.mkdir(parents=True, exist_ok=True)
    if not log_file_path.exists():
        log_file_path.touch()
        logger_config(log_file_path)
    with log_file_path.open('r') as log_file:
        history = log_file.readlines()
    return history

log_file_path = Path(settings.LOG_SUBMIT_HISTORY)
logger_config(log_file_path)
