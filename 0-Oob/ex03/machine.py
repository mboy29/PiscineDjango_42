# Imports
# -------
import random
import beverages


# Global Variables
# ----------------

ERROR = '\033[0;31m'
SUCCESS = '\033[0;32m'
INFO = '\033[0;34m'
WARNING = '\033[0;33m'
NC = '\033[0m'


# Classes
# -------

class CoffeeMachine:

    """
    CoffeeMachine class, representing a coffee machine that can serve beverages
    such as Coffee, Tea, Chocolate and Cappuccino but also an EmptyCup.
    Can break down after serving 10 drinks and needs to be repaired.
    """

    def __init__(self):

        """
        Method to initialize the CoffeeMachine object,
        setting the broken status and the number of served drinks.

        Parameters: None

        Returns: None
        """

        self.broken = False
        self.served_drinks = 0
    
            
    class EmptyCup(beverages.HotBeverage):

        """
        EmptyCup class, inheriting from HotBeverage and representing an empty cup
        with a price and a name.
        """
        
        def __init__(self):

            """
            Method to initialize the EmptyCup object, inheriting from 
            HotBeverage and setting the price and the name.
            
            Parameters: None

            Returns: None
            """

            super().__init__(name="empty cup", price=0.90)
        
        def description(self) -> str:

            """
            Method to return the description of the EmptyCup object.

            Parameters: None

            Returns:
                - str: The description of the EmptyCup object.
            """

            return "An empty cup?! Gimme my money back!"
        
    class BrokenMachineException(Exception):

        """
        BrokenMachineException class, inherites from Exception and represents
        an exception raised when a CoffeeMachine object is broken.
        """
            
        def __init__(self):

            """
            Method to initialize the BrokenMachineException object.

            Parameters: None

            Returns: None
            """

            super().__init__("This coffee machine has to be repaired.")
    
    def repair(self):

        """
        Method to repair the CoffeeMachine object by setting the broken
        status to False and the number of served drinks to 0.

        Parameters: None

        Returns: None
        """

        self.broken = False
        self.served_drinks = 0
    
    def serve(self, beverage: beverages.HotBeverage) -> None:

        """
        Method to serve a beverage from the CoffeeMachine object.
        If the machine has served 10 drinks and breaks or is already 
        broken, raises a BrokenMachineException.
        Else, increments the number of served drinks and serves a beverage 
        (randomly returns a emptyCup or the beverages asked for).

        Parameters:
            beverage (HotBeverage) - The beverage to serve.
        
        Returns: None
        """

        if self.served_drinks >= 10:
            self.broken = True
        if self.broken:
            raise self.BrokenMachineException()
        
        self.served_drinks += 1
        if random.choice([True, False]):
            return beverage()
        return self.EmptyCup()
        

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
        print(f"{WARNING}[USAGE] python3 beverages.py{NC}")
    exit(code)


# Main Function
# -------------
def main() -> None:

    """
    Main function to test the CoffeeMachine class and its methods.
    Instantiates the CoffeeMachine and requests beverages until the machine 
    breaks down, repairs the machine and repeats until the machine breaks
    down again.
    Testing stops as soon as it has demonstrated twice that the breaking/fixing
    implementation is working as expected.
    
    Parameters: None
    
    Returns: None
    """
    
    breakpoint = 0
    machine = CoffeeMachine()
    beverages_list = [
        beverages.Coffee, 
        beverages.Tea, 
        beverages.Chocolate, 
        beverages.Cappuccino
    ]

    print(f"{INFO}Testing CoffeeMachine...{NC}")
    print(f"{INFO}{'-' * 21}{NC}\n")
    
    while breakpoint < 2:
        try:
            for i in range(15): 
                beverage_class = random.choice(beverages_list)
                beverage = machine.serve(beverage_class)
                print(f"{INFO}Serving Beverage {i+1}: {beverage_class.__name__}{NC}")
                print(f"{INFO}{'-' * (20 + len(beverage_class.__name__))}{NC}")
                print(beverage, end="\n\n")
        except CoffeeMachine.BrokenMachineException as e:
            print(f"{ERROR}[ERROR] {e}{NC}\n")
            print(f"{INFO}[INFO] Repairing the machine...{NC}\n")
            breakpoint += 1
            machine.repair()
            if breakpoint <= 2:
                print(f"{SUCCESS}[SUCCESS] Machine repaired.{NC}\n")
    
# Main
# ----

if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        t_err(exc)
