import logging
from datetime import datetime
from django.conf import settings

# LOGGER
# ------

logger = logging.getLogger('submit_history')

def logger_update(input_text) -> None:

    """
    Update the log file "submit_history" with an new entry,
    containing the input text and a timestamp.

    Args:
        input_text (str): the text to be added to the log file.
    
    Returns:
        None
    """

    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    logger.info(f'{timestamp} - {input_text}') 

def logger_read() -> list:

    """
    Read the log file "submit_history" and return its content
    as a list.
    
    Args:
        None
    
    Returns:
        list: the content of the log file.
    """

    history = []
    log_file_path = settings.LOG_SUBMIT_HISTORY
    if log_file_path.exists():
        with open(log_file_path, 'r') as log_file:
            history = log_file.readlines()
    return history