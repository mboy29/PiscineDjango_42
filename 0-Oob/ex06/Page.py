# Imports
# -------
from elements import *


# Global Variables
# ----------------

ERROR = '\033[0;31m'
SUCCESS = '\033[0;32m'
INFO = '\033[0;34m'
WARNING = '\033[0;33m'
NC = '\033[0m'


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
    

    def __str__(self) -> str:
        
        """
        The __str__() method used to output the HTML page as a string.

        Parameters: None

        Returns:
            - str: The HTML page as a string.
        """

        doctype = "<!DOCTYPE html>\n" if isinstance(self.element, Html) else ""
        return doctype + str(self.element)

    def is_valid(self) -> bool:

        """
        Method that checks if the HTML structure is valid by recursively
        checking the structure starting from the provided element.

        Parameters: None

        Return:
            - bool: True if the HTML structure is valid, False otherwise.
        """

        return self.is_valid_recursively(self.element)

    def is_valid_recursively(self, elem=None) -> bool:
        
        """
        Recursively validates the HTML structure starting from the provided element.

        Parameters:
            - elem (Elem): The element to validate recursively. Defaults to self.element.

        Returns:
            - bool: True if the HTML structure starting from elem is valid, False otherwise.
        """
        
        if elem is None:
            elem = self.element
        
        def is_valid_recursively_node() -> bool:
            
            """
            Check if the element is a valid Elem :
            - Html ;            - Th ;          - H2 ;
            - Head ;            - Tr ;          - P ;
            - Body ;            - Td ;          - Div ;
            - Title ;           - Ul ;          - Span ;
            - Meta ;            - Ol ;          - Hr ;
            - Img ;             - Li ;          - Br ;
            - Table ;           - H1 ;          - Text.
            
            Returns:
                - bool: True if the element is valid Elem, False otherwise.
            """
            
            if not isinstance(elem, (Html, Head, Body, Title, Meta, Img, Table, Th, Tr, Td, Ul, Ol, Li, H1, H2, P, Div, Span, Hr, Br, Text)):
                return False
            return True

        def is_valid_recursively_html(elem) -> bool:
            
            """
            Check if a Html Elem is valid : must strictly contain a Head, then a Body.
            
            Returns:
                - bool: True if the Html is valid, False otherwise.
            """
            
            if isinstance(elem, Html):
                if len(elem.content) != 2:
                    return False
                elif (not isinstance(elem.content[0], Head) or 
                      not isinstance(elem.content[1], Body)):
                    return False
                return all(self.is_valid_recursively(el) for el in elem.content)
            return True

        def is_valid_recursively_head(elem) -> bool:
            
            """
            Check if the Head Elem is valid : must strictly contain a Title.
            
            Returns:
                - bool: True if the Head is valid, False otherwise.
            """
            
            if isinstance(elem, Head):
                if sum(1 for el in elem.content if isinstance(el, Title)) != 1:
                    return False
                return all(self.is_valid_recursively(el) for el in elem.content)
            return True

        def is_valid_recursively_body_div(elem) -> bool:
            
            """
            Check if the Body or Div Elem is valid : must strictly contain
            elements H1, H2, Div, Table, Ul, Ol, Span, or Text.
            
            Returns:
                - bool: True if the Body or Div is valid, False otherwise.
            """
            
            if isinstance(elem, (Body, Div)):
                for el in elem.content:
                    if not isinstance(el, (H1, H2, Div, Table, Ul, Ol, Span, Text)):
                        return False
                return all(self.is_valid_recursively(el) for el in elem.content)
            return True

        def is_valid_recursively_text(elem) -> bool:
            
            """
            Check if text content elements such as Title, H1, H2, Li, Th, Td
            are valid: must only and strictly contain one Text elements.
            
            Returns:
                - bool: True if the text content is valid, False otherwise.
            """
            
            if isinstance(elem, (Title, H1, H2, Li, Th, Td)):
                if len(elem.content) != 1 or not isinstance(elem.content[0], Text):
                    return False
            return True

        def is_valid_recursively_paragraph(elem) -> bool:
            
            """
            Check if the P Elem is valid : must strictly contain Text elements.
            
            Returns:
                - bool: True if the P is valid, False otherwise.
            """
            
            if isinstance(elem, P):
                return all(isinstance(el, Text) for el in elem.content)
            return True

        def is_valid_recursively_span(elem) -> bool:
            
            """
            Check if the Span Elem is valid : must only contain Text or some P elements.
            
            Returns:
                - bool: True if the Span is valid, False otherwise.
            """
            
            if isinstance(elem, Span):
                for el in elem.content:
                    if not isinstance(el, (Text, P)):
                        return False
                return all(self.is_valid_recursively(el) for el in elem.content)
            return True

        def is_valid_recursively_list(elem) -> bool:
            
            """
            Check if the Ul or Ol Elem is valid : must strictly contain at least one Li element.
            
            Returns:
                - bool: True if the Ul or Ol is valid, False otherwise.
            """
            
            if isinstance(elem, (Ul, Ol)):
                if len(elem.content) == 0:
                    return False
                for el in elem.content:
                    if not isinstance(el, Li):
                        return False
                return all(self.is_valid_recursively(el) for el in elem.content)
            return True

        def is_valid_recursively_table_row(elem) -> bool:
            
            """
            Checks if the Tr, Th, or Td elements are valid:
            - Tr must contain at least one Th or Td and only some Th or Td;
            - Th and Td must be mutually exclusive.
            
            Returns:
                - bool: True if the Tr, Th, or Td are valid, False otherwise.
            """

            if isinstance(elem, Tr):
                if not elem.content:
                    return False
                
                contains_th = any(isinstance(item, Th) for item in elem.content)
                contains_td = any(isinstance(item, Td) for item in elem.content)
                
                if contains_th and contains_td:
                    return False
        
                return all(self.is_valid_recursively(el) for el in elem.content)
                   
            return True

        def is_valid_recursively_table(elem) -> bool:
            
            """
            Check if the Table Elem is valid : must strictly contain Tr elements.
            
            Returns:
                - bool: True if the Table is valid, False otherwise.
            """

            if isinstance(elem, Table):
                for el in elem.content:
                    if not isinstance(el, Tr):
                        return False
                return all(self.is_valid_recursively(el) for el in elem.content)
            return True
        
        if not is_valid_recursively_node():
            return False
        elif isinstance(elem, Text) or isinstance(elem, Meta):
            return True
        elif isinstance(elem, Html):
            return is_valid_recursively_html(elem)
        elif isinstance(elem, Head):
            return is_valid_recursively_head(elem)
        elif isinstance(elem, Body) or isinstance(elem, Div):
            return is_valid_recursively_body_div(elem)
        elif isinstance(elem, Title) or isinstance(elem, H1) or isinstance(elem, H2) or isinstance(elem, Li) \
                or isinstance(elem, Th) or isinstance(elem, Td):
            return is_valid_recursively_text(elem)
        elif isinstance(elem, P):
            return is_valid_recursively_paragraph(elem)
        elif isinstance(elem, Span):
            return is_valid_recursively_span(elem)
        elif isinstance(elem, Ul) or isinstance(elem, Ol):
            return is_valid_recursively_list(elem)
        elif isinstance(elem, Tr):
            return is_valid_recursively_table_row(elem)
        elif isinstance(elem, Table):
            return is_valid_recursively_table(elem)
        return False


    def write_to_file(self, file_path: str) -> None:
       
        """
        Write the HTML code to a file.

        Parameters:
            - filename (str): The name of the file to write to.
        
        Returns: None
        """
        
        with open(file_path, 'w') as file:
            file.write(str(self))


# Test Functions
# --------------

def test_valid_page() -> None:

    """
    Function to test the Page class with a valid HTML document
    (tests initialization, validation, output and writing to file).

    Parameters: None

    Returns: None
    """

    print(f"{INFO}Test 1: Valid HTML Document{NC}")
    print(f"{INFO}{'-' * 27}{NC}")
    
    try:
        html = Html([
            Head(Title(Text("Example Title"))),
            Body([
                H1(Text("Header 1")),
                Div([
                    H1(Text("Header 1")),
                    H2(Text("Header 2")),
                ]),
                Table([
                    Tr([
                        Th(Text("Header 1")),
                        Th(Text("Header 2"))
                    ]),
                    Tr([
                        Td(Text("Data 1")),
                        Td(Text("Data 2"))
                    ])
                ])
            ])
        ])
        
        page = Page(html)
        if not page.is_valid():
            raise Exception("Validation failed")
        
        print(f"{SUCCESS}[SUCCESS] Validation passed{NC}")
        print(f"{SUCCESS}[INFO] Content:{NC}\n{str(page)}")
        
        page.write_to_file("valid_output.html")
        print(f"{SUCCESS}[SUCCESS] HTML written to file{NC}")
    
    except Exception as exc:
        print(f"{ERROR}[ERROR] {exc}{NC}")

def test_valid_table_structure() -> None:
    
    """
    Function to test the Page class with a valid table structure.

    Parameters: None

    Returns: None 
    """
    
    print(f"{INFO}Test 6: Valid Table Structure{NC}")
    print(f"{INFO}{'-' * 30}{NC}")
    
    try:
        html = Html([
            Head(Title(Text("Example Title"))),
            Body([
                Table([
                    Tr([
                        Th(Text("Header 1")),
                        Th(Text("Header 2"))
                    ]),
                    Tr([
                        Td(Text("Data 1")),
                        Td(Text("Data 2"))
                    ])
                ])
            ])
        ])
        
        page = Page(html)
        
        if not page.is_valid():
            raise Exception("Validation failed")

        print(f"{SUCCESS}[SUCCESS] Validation passed{NC}")
        print(f"{SUCCESS}[INFO] Content:{NC}\n{str(page)}")
        
        page.write_to_file("valid_table_output.html")
        print(f"{SUCCESS}[SUCCESS] HTML written to file{NC}")
    
    except Exception as exc:
        print(f"{ERROR}[ERROR] {exc}{NC}")

def test_invalid_page_missing_head() -> None:

    """
    Function to test the Page class with an invalid HTML document, 
    and more specifically, a missing Head element (tests validation 
    (tests initialization, validation, output and writing to file).

    The function is expected to raise an exception when the HTML and
    print an error.

    Parameters: None

    Returns: None 
    """

    print(f"{INFO}Test 2: Invalid HTML Document (Missing Head){NC}")
    print(f"{INFO}{'-' * 45}{NC}")
    
    try:
        html = Html([
            Body([
                H1(Text("Header 1")),
                P(Text("This is a paragraph.")),
                Img()
            ])
        ])
        
        page = Page(html)
        if not page.is_valid():
            raise Exception("Validation should have failed")

        print(f"{ERROR}[ERROR] Validation did not fail as expected{NC}")
    
    except Exception as exc:
        print(f"{SUCCESS}[SUCCESS] Validation failed as expected: {exc}{NC}")

def test_invalid_page_invalid_node_in_body() -> None:
    
    """
    Function to test the Page class with an invalid HTML document, 
    specifically with an invalid node in the Body.

    The function is expected to raise an exception when the HTML and
    print an error.

    Parameters: None

    Returns: None 
    """
    
    print(f"{INFO}Test 3: Invalid HTML Document (Invalid Node in Body){NC}")
    print(f"{INFO}{'-' * 49}{NC}")
    
    try:
        html = Html([
            Head(Title(Text("Example Title"))),
            Body([
                H1(Text("Header 1")),
                P(Text("This is a paragraph.")),
            ])
        ])
        
        page = Page(html)
        
        if not page.is_valid():
            raise Exception("Validation should have failed")

        print(f"{ERROR}[ERROR] Validation did not fail as expected{NC}")
    
    except Exception as exc:
        print(f"{SUCCESS}[SUCCESS] Validation failed as expected: {exc}{NC}")


def test_invalid_element_in_span() -> None:
    
    """
    Function to test the Page class with an invalid element within a Span.

    The function is expected to raise an exception and print an error.

    Parameters: None

    Returns: None 
    """

    print(f"{INFO}Test 4: Invalid Element in Span{NC}")
    print(f"{INFO}{'-' * 31}{NC}")
    
    try:
        html = Html([
            Head(Title(Text("Example Title"))),
            Body([
                Span([
                    P(Text("This is a paragraph.")),
                    Img()  # Invalid element in Span
                ])
            ])
        ])
        
        page = Page(html)
        if not page.is_valid():
            raise Exception("Validation should have failed")

        print(f"{ERROR}[ERROR] Validation did not fail as expected{NC}")
    
    except Exception as exc:
        print(f"{SUCCESS}[SUCCESS] Validation failed as expected: {exc}{NC}")

def test_empty_list_elements() -> None:
    
    """
    Function to test the Page class with empty list elements (Ul and Ol).

    The function is expected to raise an exception and print an error.

    Parameters: None

    Returns: None 
    """
    
    print(f"{INFO}Test 5: Empty List Elements{NC}")
    print(f"{INFO}{'-' * 27}{NC}")
    try:
        html = Html([
            Head(Title(Text("Example Title"))),
            Body([
                Ul([]),
                Ol([]) 
            ])
        ])
        page = Page(html)
        if not page.is_valid():
            raise Exception("Validation should have failed")

        print(f"{ERROR}[ERROR] Validation did not fail as expected{NC}")
    
    except Exception as exc:
        print(f"{SUCCESS}[SUCCESS] Validation failed as expected: {exc}{NC}")

def test_invalid_table_structure() -> None:
    
    """
    Function to test the Page class with an invalid table structure 
    (mixing Th and Td elements in the same row).

    The function is expected to raise an exception and print an error.

    Parameters: None

    Returns: None 
    """
    
    print(f"{INFO}Test 7: Invalid Table Structure (Th and Td mixed){NC}")
    print(f"{INFO}{'-' * 50}{NC}")
    
    try:
        html = Html([
            Head(Title(Text("Example Title"))),
            Body([
                Table([
                    Tr([
                        Th(Text("Header 1")),
                        Td(Text("Data 1"))  # Mixing Th and Td
                    ])
                ])
            ])
        ])
        page = Page(html)
        if not page.is_valid():
            raise Exception("Validation should have failed")

        print(f"{ERROR}[ERROR] Validation did not fail as expected{NC}")
    
    except Exception as exc:
        print(f"{SUCCESS}[SUCCESS] Validation failed as expected: {exc}{NC}")


# Main Function
# -------------

def     main() -> None:

    """
    Main funtion used to demonstrate how the Page class works
    by executing a series of tests.

    Parameters: None

    Returns: None
    """
   
    test_valid_page()
    print("\n")
    test_valid_table_structure()
    print("\n")
    test_invalid_page_missing_head()
    print("\n")
    test_invalid_page_invalid_node_in_body()
    print("\n")
    test_invalid_element_in_span()
    print("\n")
    test_empty_list_elements()
    print("\n")
    test_invalid_table_structure()
    

# Main
# ----

if __name__ == '__main__':
    try:
        main()
        
    except Exception as exc:
        print(exc)