# Imports
# -------
import sys

# Classes
# -------
# Classes
# -------

class HotBeverage:

    """
    HotBeverage class, representing a hot beverage with a price and a name.
    """

    def __init__(self, price=0.30, name="hot beverage"):

        """
        Method to initialize the HotBeverage object,
        setting the price and the name of the hot beverage.

        Parameters:
            price (float) - The price of the hot beverage, defaults to 0.30.
            name (str) - The name of the hot beverage, defaults to "hot beverage".
        
        Returns: None
        """

        self.price = price
        self.name = name
    
    def __str__(self) -> str:

        """
        Method to return the string representation of the HotBeverage object
        (name, price and description)

        Parameters: None

        Returns:
            - str: The string representation of the HotBeverage object.
        """

        return (
            f"name : {self.name}\n"
            f"price : {self.price:.2f}\n"
            f"description : {self.description()}"
        )

    def description(self) -> str:

        """
        Method to return the description of the HotBeverage object.

        Parameters: None

        Returns:
            - str: The description of the HotBeverage object.
        """

        return "Just some hot water in a cup."

class Coffee(HotBeverage):
    
    """
    Coffee class, inheriting from HotBeverage and representing a coffee
    with a price and a name.
    """

    def __init__(self, price=0.40, name="coffee"):

        """
        Method to initialize the Coffee object, inheriting from HotBeverage
        and setting the price and the name.
        
        Parameters:
            price (float) - The price of the coffee, defaults to 0.40.
            name (str) - The name of the coffee, defaults to "coffee".
        
        Returns: None
        """

        super().__init__(price, name)

    def description(self) -> str:

        """
        Method to return the description of the Coffee object.

        Parameters: None

        Returns:
            - str: The description of the Coffee object.
        """

        return "A coffee, to stay awake."

class Tea(HotBeverage):
    
    """
    Tea class, inheriting from HotBeverage and representing a tea
    with a price and a name.
    """
    
    def __init__(self, price=0.30, name="tea"):

        """
        Method to initialize the Tea object, inheriting from HotBeverage
        and setting the price and the name.

        Parameters:
            price (float) - The price of the tea, defaults to 0.40.
            name (str) - The name of the tea, defaults to "tea".
        
        Returns: None
        """
        
        super().__init__(price, name)

class Chocolate(HotBeverage):
    
    """
    Chocolate class, inheriting from HotBeverage and representing a chocolate
    with a price and a name.
    """
        
    def __init__(self, price=0.50, name="chocolate"):

        """
        Method to initialize the Chocolate object, inheriting from HotBeverage
        and setting the price and the name.

        Parameters:
            price (float) - The price of the chocolate, defaults to 0.40.
            name (str) - The name of the chocolate, defaults to "chocolate".
        
        Returns: None
        """

        super().__init__(price, name)

    def description(self) -> str:

        """
        Method to return the description of the Chocolate object.

        Parameters: None

        Returns:
            - str: The description of the Chocolate object.
        """

        return "Chocolate, sweet chocolate..."

class Cappuccino(HotBeverage):
        
    """
    Cappuccino class, inheriting from HotBeverage and representing a cappuccino
    with a price and a name.
    """
    
    def __init__(self, price=0.45, name="cappuccino"):

        """
        Method to initialize the Cappuccino object, inheriting from HotBeverage
        and setting the price and the name.

        Parameters:
            price (float) - The price of the cappuccino, defaults to 0.40.
            name (str) - The name of the cappuccino, defaults to "cappuccino".

        Returns: None
        """

        super().__init__(price, name)

    def description(self) -> str:

        """
        Method to return the description of the Cappuccino object.

        Parameters: None

        Returns:
            - str: The description of the Cappuccino object.
        """
        
        return "Un po’ di Italia nella sua tazza!"
    

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
        print("\033[0;33m[USAGE] python3 beverages.py\033[0m")
    exit(code)


# Functions
# ---------

def test() -> None:

    """
    Function to test classes and their methods:
    - HotBeverage;
    - Coffee;
    - Tea;
    - Chocolate;
    - Cappuccino.
    
    Parameters: None

    Returns: None
    """

    try:
        beverages = [
            HotBeverage(),
            Coffee(),
            Tea(),
            Chocolate(),
            Cappuccino(),
        ]

        for beverage in beverages:
            if beverage == beverages[-1]:
                print(beverage)
            else:
                print(beverage, end="\n\n")

    except Exception as e:
        print(e)


# Main Function
# -------------

def main(arg: list) -> None:

    """
    Main function of the script to test all classes
    initiated beforehand.

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
