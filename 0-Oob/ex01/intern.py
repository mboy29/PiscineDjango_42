# Imports
# -------
import sys


# Global Variables
# ----------------

ERROR = '\033[0;31m'
SUCCESS = '\033[0;32m'
INFO = '\033[0;34m'
WARNING = '\033[0;33m'
NC = '\033[0m'


# Classes
# -------

class Coffee:

    """
    Coffee class, representing a coffee.
    """

    def __str__(self) -> str:
        
        """
        Method to return the string representation of the Coffee object.

        Parameters: None

        Returns: 
            - str: The string representation of the Coffee object.
        """
       
        return "This is the worst coffee you ever tasted."


class Intern:
    
    """
    Intern class, representing an intern with a name and the ability to make 
    coffee but not to work.
    """

    def __init__(self, name="My name? I’m nobody, an intern, I have no name."):
       
        """
        Constructor of the Intern class, sets the name of the intern.

        Parameters:
            name (str) - The name of the intern, defaults to 
                "My name? I’m nobody, an intern, I have no name.".
        
        Returns: None
        """
    
        self.name = name

    def __str__(self):
        
        """
        Method to return the string representation of the Intern object.

        Parameters: None

        Returns: 
            - str: The string representation of the Intern object.
        """

        return self.name

    def work(self):
        
        """
        Method to simulate the work of the intern.

        Parameters: None

        Returns: None
        """

        raise Exception("I’m just an intern, I can’t do that...")

    def make_coffee(self):
        
        """
        Method to make coffee.

        Parameters: None

        Returns: 
            - Coffee: A Coffee object.
        """
    
        return Coffee()


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
        print(f"{WARNING}[USAGE] python3 intern.py{NC}")
    exit(code)


# Main Function
# -------------

def main() -> None:

    """
    Main function to test the Intern class and its methods:
    - Instantiate the Intern class without a name;
    - Instantiate the Intern class with the name "Mark";
    - Ask Mark to make coffee.
    - Ask the other intern to work.

    Parameters: None

    Returns: None
    """

    try:
        print(f"{INFO}Test 1: Instantiate the Intern class without a name{NC}")
        print(f"{INFO}---------------------------------------------------{NC}")
        other = Intern()
        print(other)

        print(f"\n{INFO}Test 2: Instantiate the Intern class with the name 'Mark'{NC}")
        print(f"{INFO}---------------------------------------------------------{NC}")
        mark = Intern("Mark")
        print(mark)

        print(f"\n{INFO}Test 3: Ask Mark to make coffee{NC}")
        print(f"{INFO}--------------------------------{NC}")
        coffee = mark.make_coffee()
        print(coffee)

        print(f"\n{INFO}Test 4: Ask other intern to work{NC}")
        print(f"{INFO}--------------------------------{NC}")
        other.work()
    except Exception as exc:
        print(exc)


# Main
# ----

if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        t_err(exc)
