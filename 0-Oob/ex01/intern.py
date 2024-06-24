# Imports
# -------
import sys

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
    
    print(f"\033[0;31m[ERROR] {msg}\033[0m")
    if usage:
        print("\033[0;33m[USAGE] python3 intern.py\033[0m")
    exit(code)


# Functions
# ---------

def test() -> None:

    """
    Function to test the Intern class and its methods:
    - Instantiate the Intern class without a name;
    - Instantiate the Intern class with the name "Mark";
    - Ask Mark to make coffee.

    Parameters: None

    Returns: None
    """

    try:
        intern1 = Intern()
        print(intern1)

        intern2 = Intern("Mark")
        print(intern2)

        coffee = intern2.make_coffee()
        print(coffee)

        intern1.work()
    except Exception as e:
        print(e)


# Main Function
# -------------

def main(arg: list) -> None:

    """
    Main function of the script to test the Intern class.

    Parameters:
        arg (list) - The list of arguments.
    
    Returns: None
    """

    if len(arg) != 0:
        t_err("Invalid number of arguments", True)
    test()
    
    

# Main
# ----

if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    except Exception as exc:
        t_err(exc)
