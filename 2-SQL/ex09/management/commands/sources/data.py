import json, os

def data_open(file_path):
    
    """
    Open the JSON file for reading.
    
    Args:
        file_path (str): Path to the JSON file.
    
    Returns:
        file object: The opened file object.
    """
    
    try:
        return open(file_path, 'r')
    except FileNotFoundError:
        raise FileNotFoundError(f'File {file_path} not found.')
    except Exception as e:
        raise Exception(f'An error occurred while opening the file: {e}')

def data_close(file):
    
    """
    Close the opened file.
    
    Args:
        file (file object): The opened file object.
    
    Returns:
        None
    """
    
    try:
        file.close()
    except Exception as e:
        raise Exception(f'An error occurred while closing the file: {e}')

def data_read(file_path):
    
    """
    Open, read, and close the JSON file.
    
    Args:
        file (file object): The opened file object.
    
    Returns:
        dict: Parsed JSON data from the file.
    
    Raises:
        json.JSONDecodeError: If an error occurs while decoding JSON data.
        Exception: If an error occurs while reading the file
    """
    
    try:
        file = data_open(file_path)
        data = json.load(file)
        data_close(file)
        return data
    except json.JSONDecodeError:
        raise ValueError('Error decoding JSON data.')
    except Exception as e:
        raise Exception(f'An error occurred while reading the file: {e}')