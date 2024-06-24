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
        print("\033[0;33m[USAGE] python3 var_to_dict.py\033[0m")
    exit(code)


# Functions
# ---------

def var_to_dict(lst: list) -> dict:

    """
    Converts a list of tuples into a dictionary and
    swaps the keys and values.

    Parameters:
        lst (list) - The list of tuples to convert.

    Returns:
        dict - The dictionary created from the list.
    """

    return {v: k for k, v in dict(lst).items()}


# Main Function
# -------------

def main() -> None:
    
    """
    Main function of the script to convert a list of tuples
    into a dictionary and swap the keys and values.

    Parameters: None
    
    Returns: None
    """

    # Define given list
    d = [
        ('Hendrix' , '1942'),
        ('Allman' , '1946'),
        ('King' , '1925'),
        ('Clapton' , '1945'),
        ('Johnson' , '1911'),
        ('Berry' , '1926'),
        ('Vaughan' , '1954'),
        ('Cooder' , '1947'),
        ('Page' , '1944'),
        ('Richards' , '1943'),
        ('Hammett' , '1962'),
        ('Cobain' , '1967'),
        ('Garcia' , '1942'),
        ('Beck' , '1944'),
        ('Santana' , '1947'),
        ('Ramone' , '1948'),
        ('White' , '1975'),
        ('Frusciante', '1970'),
        ('Thompson' , '1949'),
        ('Burton' , '1939')
    ]

    converted = var_to_dict(d)
    for k, v in converted.items():
        print(f"{k} : {v}")
    
    
# Main
# ----

if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        t_err(exc)