# Imports
# -------
import sys


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

    print(f"\033[0;31m[ERROR] {msg}\033[0m")
    if usage == True:
        print("\033[0;33m[USAGE] python3 numbers.py <path to file>\033[0m")
    exit(code)

def t_open(path: str) -> str:

    """
    Opens a file and returns its content. 
    Also checks if the file exists, is not a directory and 
    is readable.

    Parameters:
        path (str) - The path to the file to open.

    Returns:
        str - The content of the file.
    """

    try:
        with open(path, "r") as f:
            return f.read()
    except FileNotFoundError:
        raise Exception(f"'{path}' does not exist.")
    except IsADirectoryError:
        return t_err(f"'{path}' is a directory.")
    except PermissionError:
        return t_err(f"No permission to read '{path}'.")


# Main Function
# -------------

def main(arg: list) -> None:

    """
    Main function of the program : opens a file and prints
    the numbers it contains excluding the commas in between.

    Parameters:
        arg (list) - List of arguments given to the program.

    Returns: None
    """

    # Check number of arguments
    if len(arg) != 1:
        t_err("Invalid number of arguments", True)
    
    # Open file and print numbers
    file_content = t_open(arg[0])
    numbers = file_content.split(",")
    for number in numbers:
        print(number.strip())
    

# Main
# ----

if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    except Exception as exc:
        t_err(exc)