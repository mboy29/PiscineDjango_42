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
            Check if the element is a valid Elem :
            - Html ;            - Th ;          - H2 ;
            - Head ;            - Tr ;          - P ;
            - Body ;            - Td ;          - Div ;
            - Title ;           - Ul ;          - Span ;
            - Meta ;            - Ol ;          - Hr ;
            - Img ;             - Li ;          - Br ;
            - Table ;           - H1 ;          - Text.
            
            Parameters: None

            Returns:
                - bool: True if the element is valid Elem, False otherwise.
            """

            if not isinstance(self.element, (Html, Head, Body, Title, Meta, Img, Table, Th, Tr, Td, Ul, Ol, Li, H1, H2, P, Div, Span, Hr, Br, Text)):
                return False
            return True
        
        def is_valid_html(self) -> bool:

            """
            Check if a Html Elem is valid : must strictly contain a Head, then a Body.

            Parameters: None

            Returns:
                - bool: True if the Html is valid, False otherwise.
            """

            if isinstance(self.element, Html):
                if len(self.element.content) != 2: 
                    return False
                for item in self.element.content:
                    if not isinstance(item, (Head, Body)):
                        return False
            return True

        def is_valid_head(self) -> bool:

            """
            Check if the Head Elem is valid : must strictly contain a Title.

            Parameters: None

            Returns:
                - bool: True if the Head is valid, False otherwise.
            """

            if isinstance(self.element, Head):
                if len(self.element.content) != 1:
                    return False
                elif not isinstance(self.element.content[0], Title):
                    return False
            return True
    
        def is_valid_body_div(self) -> bool:

            """
            Check if the Body or Div Elem is valid : must strictly contain
            elements H1, H2, Div, Table, Ul, Ol, Span, or Text.

            Parameters: None

            Returns:
                - bool: True if the Body or Div is valid, False otherwise.
            """
            
            if isinstance(self.element, (Body, Div)):
                for item in self.element.content:
                    if not isinstance(item, (H1, H2, Div, Table, Ul, Ol, Span, Text)):
                        return False
            return True

        def is_valid_text(self) -> bool:

            """
            Check if text content elements such as Title, H1, H2, Li, Th, Td
            are valid: must only and strickly contain one Text elements.
            
            Parameters: None

            Returns:
                - bool: True if the text content is valid, False otherwise.
            """

            if isinstance(self.element, (Title, H1, H2, Li, Th, Td)):
                if len(self.element.content) != 1:
                    return False
                elif not isinstance(self.element.content[0], Text):
                    return False
            return True
        
        def is_valid_paragraph(self) -> bool:

            """
            Check if the P Elem is valid : must strictly contain Text elements.

            Parameters: None

            Returns:
                - bool: True if the P is valid, False otherwise.
            """

            if isinstance(self.element, P):
                for item in self.element.content:
                    if not isinstance(item, Text):
                        return False
            return True

        def is_valid_span(self) -> bool:

            """
            Check if the Span Elem is valid : must only contain Text or some P 
            elements.
            
            Parameters: None

            Returns:
                - bool: True if the Span is valid, False otherwise.
            """

            if isinstance(self.element, Span):
                for item in self.element.content:
                    if not isinstance(item, (Text, P)):
                        return False
            return True

        def is_valid_list(self) -> bool:

            """
            Check if the Ul or Ol Elem is valid : must strictly contain at least on 
            Li element.

            Parameters: None

            Returns:
                - bool: True if the Ul or Ol is valid, False otherwise.
            """

            if isinstance(self.element, (Ul, Ol)):
                if len(self.element.content) == 0:
                    return False
                for item in self.element.content:
                    if not isinstance(item, Li):
                        return False
            return True

        def is_valid_table_row(self) -> bool:

            """
            Checks if the Tr, Th, or Td elements are valid: 
            - Tr must contain at least one Th or Td and only some Th or Td;
            - Th and Td must be mutually exclusive.

            Parameters: None

            Returns:
                - bool: True if the Tr, Th, or Td are valid, False otherwise.
            """
            
            if isinstance(self.element, Tr):
                if not self.element.content:
                    return False
                
                contains_th = any(isinstance(item, Th) for item in self.element.content)
                contains_td = any(isinstance(item, Td) for item in self.element.content)
                
                # Check if Th and Td are mutually exclusive
                if contains_th and contains_td:
                    return False
                
                # Ensure all elements are either Th or Td
                if not all(isinstance(item, (Th, Td)) for item in self.element.content):
                    return False
            
            return True

        def is_valid_table(self) -> bool:
                
            """
            Check if the Table Elem is valid : must strictly contain Tr elements.

            Parameters: None

            Returns:
                - bool: True if the Table is valid, False otherwise.
            """

            if isinstance(self.element, Table):
                for item in self.element.content:
                    if not isinstance(item, Tr):
                        return False
            return True
        
        validation_methods = [
            self.is_valid_node,
            self.is_valid_html,
            self.is_valid_head,
            self.is_valid_body_div,
            self.is_valid_text,
            self.is_valid_paragraph,
            self.is_valid_span,
            self.is_valid_list,
            self.is_valid_table_row
        ]
        
        return all(method() for method in validation_methods)


# Example usage and testing
if __name__ == '__main__':
    try:
        # Creating a valid HTML document
        html = Tr([
            Td(Text("Header 1")),
            Td(Text("Header 2"))
        ])
        page = Page(html)

        # Validate the HTML document
        print("Is the HTML document valid?", page.is_valid())

        # # Print the HTML document
        # print(page)

        # # Write the HTML document to a file
        # page.write_to_file("output.html")
        
    except Exception as exc:
        print(exc)