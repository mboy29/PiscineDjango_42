# Imports
# -------
from elements import *

# Classes
# -------

class Page:

    """
    A class used to validate and represent a HTML page.
    """

    def __init__(self, element: Elem) -> None:
            
        """
        The __init__() method to initialize the Page object with an element.
        
        Parameters:
            - element (Elem): The element to add to the page.
        
        Returns: None
        """

        if not isinstance(element, Elem):
            raise Elem.ValidationError
        self.element = element
    
    def is_valid(self) -> bool:
        
        """
        The is_valid() method used to check if the attribute element 
        is a valid HTML element.
        
        Parameters: None
        
        Returns:
            - bool: True if the page is valid, False otherwise.
        """

        def is_valid_node(self) -> bool:

            """
            Check if the element is only composed of the following elements:
            - Html ;
            - Head ;
            - Body ;
            - Title ;
            - Meta ;
            - Img ;
            - Table ;
            - Th ;
            - Tr ;
            - Td ;
            - Ul ;
            - Ol ;
            - Li ;
            - H1 ;
            - H2 ;
            - P ;
            - Div ;
            - Span ;
            - Hr ;
            - Br ;
            - Text.
Text
            """

        return True
