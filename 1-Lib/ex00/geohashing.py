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

    try:

        try: latitude = float(args[0])
        except ValueError: raise Exception("Invalid argument, latitude must be a float")

        try: lon = float(args[1])
        except ValueError: raise Exception("Invalid argument, longitude must be a float")

        try: djia = float(args[3])
        except ValueError: raise Exception("Invalid argument, DJIA must be a float")

        try:
            date = args[2]
            split_date = date.split("-")
            if len(split_date) != 3:
                raise Exception("Invalid argument, date must be in the format YYYY-MM-DD")
            year, month, day = split_date
            if not year.isdigit() or not month.isdigit() or not day.isdigit():
                raise Exception("Invalid argument, date must be in the format YYYY-MM-DD")
            if int(year) < 0: 
                raise Exception("Invalid argument, year must be over 0")
            elif not 1 <= int(month) <= 12:
                raise Exception("Invalid argument, month must be between 1 and 12")
            elif int(month) in [1, 3, 5, 7, 8, 10, 12] and not 1 <= int(day) <= 31:
                raise Exception("Invalid argument, day must be between 1 and 31")
            elif int(month) in [2, 4, 6, 9, 11] and not 1 <= int(day) <= 30:
                raise Exception("Invalid argument, day must be between 1 and 30")
        
        except ValueError:
            raise Exception("Invalid argument, date must be a string")
        
        return latitude, lon, date, djia
    except Exception as e:
        t_err(f"Invalid arguments: {e}", usage=True)


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
