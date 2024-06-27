# Imports
# -------
import sys
from path import Path


# Global Variables
# ----------------

ERROR = '\033[0;31m'
SUCCESS = '\033[0;32m'
INFO = '\033[0;34m'
WARNING = '\033[0;33m'
NC = '\033[0m'


# Tools
# -----

def t_err(msg: str, usage: bool = False, code: int = 1) -> None:
   
    """
    Prints an error message in red and, if required, 
    the usage of the program.

    Parameters:
        msg (str) - The error message to print.
        usage (bool) - Whether to print the usage of 
            the program, defaults to False.    
        code (int) - The error code to exit, defaults
            to 1.

    Returns: None
    """
    
    print(f"{ERROR}[ERROR] {msg}{NC}")
    if usage:
        print(f"{WARNING}[USAGE] python3 my_program.py{NC}")
    exit(code)

def t_create_folder(path: str) -> None:

    """
    Creates a folder in the given path.

    Parameters:
        path (str) - The path to create the folder.

    Returns: None
    """
    
    try:
        folder_path = Path(path)
        folder_path.mkdir_p()
        print(f"{SUCCESS}[SUCCESS] Folder created: {folder_path}")
    except FileExistsError as e:
        t_err(f"Folder already exists: {e}")

def t_create_file(path: str, content: str) -> None:

    """
    Creates a file in the given path with the given content.

    Parameters:
        path (str) - The path to create the file.
        content (str) - The content of the file.
    
    Returns: None
    """

    try:
        with Path(path).open('w') as f:
            f.write(content)
        print(f"{SUCCESS}[SUCCESS] File created: {path}")
    except Exception as e:
        t_err(f"Failed to create file: {e}")
        
def t_read_file(path: str) -> str:

    """
    Reads the content of a file from the given path.

    Parameters:
        path (str) - The path to the file.

    Returns:
        str: The content of the file.
    """

    try:
        with Path(path).open('r') as f:
            content = f.read()
        print(f"{SUCCESS}[SUCCESS] File read: {path}")
        return content
    except Exception as e:
        t_err(f"Failed to read file: {e}")


# Main Function
# -------------

def main() -> None:
    
    """
    Main function to create a folder, a file and read its content.

    Parameters: None

    Returns: None
    """
    
    try:

        folder_path = "example_folder"
        file_path = f"{folder_path}/example_file.txt"
        file_content = "example"

        t_create_folder(folder_path)
        t_create_file(file_path, file_content)
        print(f"{SUCCESS}[SUCCESS] File {file_path} content: {t_read_file(file_path)}")

    except Exception as e:
        t_err(f"Exception: {e}", usage=True)


# Main
# ----

if __name__ == '__main__':
    try:
        main()
    except Exception as exc:
        t_err(f"Unhandled exception: {exc}", usage=True)
