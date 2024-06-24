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
        print("\033[0;33m[USAGE] python3 my_sort.py\033[0m")
    exit(code)


# Functions
# ---------

def my_sort(data: dict) -> dict:

    """
    Sorts a dict with the names of guitarists as keys and 
    their birth years as values by their birth years first
    and alphabetically by their names for the same birth 
    years.

    Parameters:
        data (dict) - The dict to sort.
    
    Returns:
        dict - The sorted dict.
    """

    return sorted(data.items(), key=lambda item: (item[1], item[0]))


# Main Function
# -------------

def main(arg: list) -> None:
    
    """
    Prints the state of a given capital city.

    Parameters:
        arg (list) - The list of arguments.
    
    Returns: None
    """

    # Define variables
    d = {
        'Hendrix' : '1942',
        'Allman' : '1946',
        'King' : '1925',
        'Clapton' : '1945',
        'Johnson' : '1911',
        'Berry' : '1926',
        'Vaughan' : '1954',
        'Cooder' : '1947',
        'Page' : '1944',
        'Richards' : '1943',
        'Hammett' : '1962',
        'Cobain' : '1967',
        'Garcia' : '1942',
        'Beck' : '1944',
        'Santana' : '1947',
        'Ramone' : '1948',
        'White' : '1975',
        'Frusciante': '1970',
        'Thompson' : '1949',
        'Burton' : '1939',
    }

    # Check arguments and print capital city 
    if len(arg) != 0:
        t_err("Invalid number of arguments", True)
    sorted_data = my_sort(d)
    for item in sorted_data:
        print(f"{item[0]}: {item[1]}")
    return
    
    
# Main
# ----

if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    except Exception as exc:
        t_err(exc)