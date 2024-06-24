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
        print("\033[0;33m[USAGE] python3 state.py <capital_city>\033[0m")
    exit(code)


# Functions
# ---------

def state(capital_city: str) -> str:

    """
    Returns the state of a given capital city.
    If the state is not found, returns "Unknown State".

    Parameters:
        capital_city (str) - The capital city to search for.

    Returns:
        str - The state of the capital city.
    """

    states = {
        "Oregon" : "OR",
        "Alabama" : "AL",
        "New Jersey": "NJ",
        "Colorado" : "CO"
    }
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }

    if capital_city in capital_cities.values():
        for state, abbr in states.items():
            if capital_cities[abbr] == capital_city:
                return state
    return "Unknown capital city"


# Main Function
# -------------

def main(arg: list) -> None:
    
    """
    Prints the state of a given capital city.

    Parameters:
        arg (list) - The list of arguments.
    
    Returns: None
    """

    # Check arguments and print capital city 
    if len(arg) == 1:
        print(state(arg[0]))
    
    
# Main
# ----

if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    except Exception as exc:
        t_err(exc)