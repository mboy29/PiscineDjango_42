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
        print("\033[0;33m[USAGE] python3 all_in.py <string of expressions separated by commas>\033[0m")
    exit(code)

def t_parse(arg: str) -> list:

    """
    Parses the argument passed to the program and
    converts it into a list - splitting it by commas, 
    removing any leading or trailing whitespaces, and
    capitalizing the first letter of each word.
    
    Parameters:
        arg (str) - The argument to parse.
    
    Returns:
        list - The list of parsed arguments.
    """

    nodes: list = []
    for node in arg[0].split(","):
        if node.strip() != "":
            nodes.append(node.strip().title())
    return nodes


# Getters
# ---------

def get_state(capital_city: str) -> str:

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
    return "Unknown"

def get_capital_city(state: str) -> str:

    """
    Returns the capital city of a given state.
    If the state is not found, returns "Unknown State".

    Parameters:
        state (str) - The state to search for.

    Returns:
        str - The capital city of the state.
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

    if state in states.keys():
        return capital_cities[states[state]]
    return "Unknown"


# Functions
# ---------

def all_in(keys_values: list) -> None:

    """
    Processes a list of keys or values and determines if 
    each item is a state or a capital city.

    Parameters:
        keys_values (list) - The list of keys or values.
    
    Returns:
        None

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

    for key_value in keys_values:
        state = get_state(key_value)
        capital_city = get_capital_city(key_value)
        if state != "Unknown":
            print(f"{key_value} is the capital of {state}")
        elif capital_city != "Unknown":
            print(f"{get_capital_city(key_value)} is the capital of {key_value}")
        else:
            print(f"{key_value} is neither a capital city nor a state")


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
        keys_values = t_parse(arg)
        all_in(keys_values)
    
    
# Main
# ----

if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    except Exception as exc:
        t_err(exc)