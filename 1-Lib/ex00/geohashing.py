# Imports
# -------
import sys
import antigravity


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
        print(f"{WARNING}[USAGE] python3 geohashing.py <latitude> <longitude> <YYYY-MM-DD> <DJIA opening price>{NC}")
    exit(code)


def t_parse(args: list) -> tuple:
   
    """
    Parse the input arguments into a dictionary to be used
    for geohashing such as latitude, longitude, date, and DJIA.
    Raises an exception if the number of arguments is invalid.

    Parameters:
        args (list) - The list of arguments.

    Returns:
        tuple - A tuple containing latitude, longitude, date, and DJIA.
    """
    
    if len(args) != 4:
        t_err("Invalid number of arguments", usage=True)

    lat = float(args[0])
    lon = float(args[1])
    date = args[2]
    djia = float(args[3])
    
    if not date.count('-') == 2 or len(date) != 10:
        # check if valid date
        split_date = date.split('-')
        if not len(split_date) == 3:
            raise Exception("Invalid date format")
        year, month, day = split_date
        if not year.isdigit() or not month.isdigit() or not day.isdigit():
            raise Exception("Invalid date format")
        if not 1 <= int(month) <= 12 or not 1 <= int(day) <= 31:
            raise Exception("Invalid date format")
        if not len(year) == 4 or not len(month) == 2 or not len(day) == 2:
            raise Exception("Invalid date format")

        raise Exception("Invalid date format")
    return lat, lon, date, djia


# Functions
# ---------

def geohashing(latitude: float, longitude: float, date: str, djia: float) -> None:
    
    """
    Calculate the geohash for a given date, base coordinates, and 
    DJIA opening price.

    Parameters:
        data (dict) - The dictionary containing all necessary
            elements to calculate geohash, which include 
            atitude, longitude, date, and DJIA.

    Returns:
        None
    """

    try:
        datetow = f"{date}-{str(djia)}"
        antigravity.geohash(latitude, longitude, datetow.encode())
    except Exception as e:
        t_err(f"Failed to calculate geohash: {e}")


# Main Function
# -------------

def main(args: list) -> None:
    
    """
    Main function to parse input arguments and calculate geohash.

    Returns:
        None
    """
    try:
        geohashing(*t_parse(args))
    except Exception as e:
        t_err(f"Exception: {e}", usage=True)


# Main
# ----

if __name__ == '__main__':
    try:
        main(sys.argv[1:])
    except Exception as exc:
        t_err(f"Unhandled exception: {exc}", usage=True)
