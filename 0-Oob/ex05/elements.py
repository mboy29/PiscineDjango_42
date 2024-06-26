# Imports
# -------
from elem import *


# Global Variables
# ----------------

ERROR = '\033[0;31m'
SUCCESS = '\033[0;32m'
INFO = '\033[0;34m'
WARNING = '\033[0;33m'
NC = '\033[0m'


# Classes
# -------

class Html(Elem):
    
    """
    A Html class to represent an HTML element in a web page.
    """

    def __init__(self, content=None, attr={}) -> None:
        
        """
        The __init__() method to initialize the Html object with content
        and attributes.

        Parameters:
            - content (list): The content of the HTML element.
            - attr (dict): The attributes of the HTML element.
        
        Returns: None
        """
        
        super().__init__(tag='html', content=content, attr=attr)


class Head(Elem):
    
    """
    A Head class to represent the head section of an HTML document.
    """

    def __init__(self, content=None, attr={}) -> None:
       
        """
        The __init__() method to initialize the Head object with content
        and attributes.

        Parameters:
            - content (list): The content of the head element.
            - attr (dict): The attributes of the head element.
        
        Returns: None
        """
        
        super().__init__(tag='head', content=content, attr=attr)


class Body(Elem):
   
    """
    A Body class to represent the body section of an HTML document.
    """

    def __init__(self, content=None, attr={}) -> None:
        
        """
        The __init__() method to initialize the Body object with content
        and attributes.

        Parameters:
            - content (list): The content of the body element.
            - attr (dict): The attributes of the body element.
        
        Returns: None
        """
        
        super().__init__(tag='body', content=content, attr=attr)


class Title(Elem):
    
    """
    A Title class to represent the title element of an HTML document.
    """

    def __init__(self, content=None, attr={}) -> None:
        
        """
        The __init__() method to initialize the Title object with content
        and attributes.

        Parameters:
            - content (list): The content of the title element.
            - attr (dict): The attributes of the title element.
        
        Returns: None
        """
        
        super().__init__(tag='title', content=content, attr=attr)


class Meta(Elem):
    
    """
    A Meta class to represent the meta element of an HTML document.
    """

    def __init__(self, attr={}) -> None:
        
        """
        The __init__() method to initialize the Meta object with attributes.

        Parameters:
            - attr (dict): The attributes of the meta element.
        
        Returns: None
        """
        
        super().__init__(tag='meta', attr=attr, tag_type='simple')


class Img(Elem):
    
    """
    An Img class to represent an image element in an HTML document.
    """

    def __init__(self, attr={}) -> None:
        
        """
        The __init__() method to initialize the Img object with attributes.

        Parameters:
            - attr (dict): The attributes of the image element.
        
        Returns: None
        """
        
        super().__init__(tag='img', attr=attr, tag_type='simple')


class Table(Elem):
    
    """
    A Table class to represent a table element in an HTML document.
    """

    def __init__(self, content=None, attr={}) -> None:
        
        """
        The __init__() method to initialize the Table object with content
        and attributes.

        Parameters:
            - content (list): The content of the table element.
            - attr (dict): The attributes of the table element.
        
        Returns: None
        """
        
        super().__init__(tag='table', content=content, attr=attr)


class Th(Elem):
    
    """
    A Th class to represent a table header element in an HTML document.
    """

    def __init__(self, content=None, attr={}) -> None:
        
        """
        The __init__() method to initialize the Th object with content
        and attributes.

        Parameters:
            - content (list): The content of the table header element.
            - attr (dict): The attributes of the table header element.
        
        Returns: None
        """
        
        super().__init__(tag='th', content=content, attr=attr)


class Tr(Elem):
   
    """
    A Tr class to represent a table row element in an HTML document.
    """

    def __init__(self, content=None, attr={}) -> None:
        
        """
        The __init__() method to initialize the Tr object with content
        and attributes.

        Parameters:
            - content (list): The content of the table row element.
            - attr (dict): The attributes of the table row element.
        
        Returns: None
        """
        
        super().__init__(tag='tr', content=content, attr=attr)


class Td(Elem):
   
    """
    A Td class to represent a table data element in an HTML document.
    """

    def __init__(self, content=None, attr={}) -> None:
        
        """
        The __init__() method to initialize the Td object with content
        and attributes.

        Parameters:
            - content (list): The content of the table data element.
            - attr (dict): The attributes of the table data element.
        
        Returns: None
        """
        
        super().__init__(tag='td', content=content, attr=attr)


class Ul(Elem):
    
    """
    A Ul class to represent an unordered list element in an HTML document.
    """

    def __init__(self, content=None, attr={}) -> None:
        
        """
        The __init__() method to initialize the Ul object with content
        and attributes.

        Parameters:
            - content (list): The content of the unordered list element.
            - attr (dict): The attributes of the unordered list element.
        
        Returns: None
        """
        
        super().__init__(tag='ul', content=content, attr=attr)


class Ol(Elem):
    
    """
    A Ol class to represent an ordered list element in an HTML document.
    """

    def __init__(self, content=None, attr={}) -> None:
        
        """
        The __init__() method to initialize the Ol object with content
        and attributes.

        Parameters:
            - content (list): The content of the ordered list element.
            - attr (dict): The attributes of the ordered list element.
        
        Returns: None
        """
        
        super().__init__(tag='ol', content=content, attr=attr)


class Li(Elem):
    
    """
    A Li class to represent a list item element in an HTML document.
    """

    def __init__(self, content=None, attr={}) -> None:
        
        """
        The __init__() method to initialize the Li object with content
        and attributes.

        Parameters:
            - content (list): The content of the list item element.
            - attr (dict): The attributes of the list item element.
        
        Returns: None
        """
        
        super().__init__(tag='li', content=content, attr=attr)


class H1(Elem):
    
    """
    A H1 class to represent a level 1 heading element in an HTML document.
    """

    def __init__(self, content=None, attr={}) -> None:
        
        """
        The __init__() method to initialize the H1 object with content
        and attributes.

        Parameters:
            - content (list): The content of the heading element.
            - attr (dict): The attributes of the heading element.
        
        Returns: None
        """
        
        super().__init__(tag='h1', content=content, attr=attr)


class H2(Elem):
    
    """
    A H2 class to represent a level 2 heading element in an HTML document.
    """

    def __init__(self, content=None, attr={}) -> None:
        
        """
        The __init__() method to initialize the H2 object with content
        and attributes.

        Parameters:
            - content (list): The content of the heading element.
            - attr (dict): The attributes of the heading element.
        
        Returns: None
        """
        
        super().__init__(tag='h2', content=content, attr=attr)


class P(Elem):
    
    """
    A P class to represent a paragraph element in an HTML document.
    """

    def __init__(self, content=None, attr={}) -> None:
       
        """
        The __init__() method to initialize the P object with content
        and attributes.

        Parameters:
            - content (list): The content of the paragraph element.
            - attr (dict): The attributes of the paragraph element.
        
        Returns: None
        """
        
        super().__init__(tag='p', content=content, attr=attr)


class Div(Elem):
    
    """
    A Div class to represent a division element in an HTML document.
    """

    def __init__(self, content=None, attr={}) -> None:
        
        """
        The __init__() method to initialize the Div object with content
        and attributes.

        Parameters:
            - content (list): The content of the division element.
            - attr (dict): The attributes of the division element.
        
        Returns: None
        """
        
        super().__init__(tag='div', content=content, attr=attr)


class Span(Elem):
   
    """
    A Span class to represent a span element in an HTML document.
    """

    def __init__(self, content=None, attr={}) -> None:
        
        """
        The __init__() method to initialize the Span object with content
        and attributes.

        Parameters:
            - content (list): The content of the span element.
            - attr (dict): The attributes of the span element.
        
        Returns: None
        """
        
        super().__init__(tag='span', content=content, attr=attr)


class Hr(Elem):
    
    """
    A Hr class to represent a horizontal rule element in an HTML document.
    """

    def __init__(self, attr={}) -> None:
        
        """
        The __init__() method to initialize the Hr object with attributes.

        Parameters:
            - attr (dict): The attributes of the horizontal rule element.
        
        Returns: None
        """
        
        super().__init__(tag='hr', attr=attr, tag_type='simple')


class Br(Elem):
    
    """
    A Br class to represent a line break element in an HTML document.
    """

    def __init__(self, attr={}) -> None:
        
        """
        The __init__() method to initialize the Br object with attributes.

        Parameters:
            - attr (dict): The attributes of the line break element.
        
        Returns: None
        """
        
        super().__init__(tag='br', attr=attr, tag_type='simple')


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
    Main function of the script to test the new HTML element classes
    by creating an HTML element and printing it in the console.

    Parameters: None

    Returns: None
    """
    
    try:
        print(f"{INFO}[INFO] Test 1: previous output{NC}")
        print(f"{INFO}------------------------------{NC}")
        html = Html([
            Head([
                Title(Text('"Hello ground!"'))
            ]),
            Body([
                H1(Text('"Oh no, not again!"')),
                Img(attr={'src': 'http://i.imgur.com/pfp3T.jpg'})
            ])
        ])
        print(html, end='\n\n')
        
        print(f"{INFO}[INFO] Test 2: new output{NC}")
        print(f"{INFO}-------------------------{NC}")
        html = Html([
            Head([
                Title([Text('"Hello ground!"')]),
                Meta(attr={'charset': 'UTF-8'})
            ]),
            Body([
                H1([Text('"Oh no, not again!"')]),
                Img(attr={'src': 'http://i.imgur.com/pfp3T.jpg', 'alt': 'A funny image'}),
                H2([Text('"Subheading here"')]),
                P([Text('"This is a paragraph with some text."')]),
                Div([
                    P([Text('"This is a paragraph inside a div."')]),
                    Span([Text('"This is a span inside a div."')])
                ], attr={'class': 'content'}),
                Table([
                    Tr([
                        Th([Text('"Header 1"')]),
                        Th([Text('"Header 2"')])
                    ]),
                    Tr([
                        Td([Text('"Data 1"')]),
                        Td([Text('"Data 2"')])
                    ])
                ]),
                Ul([
                    Li([Text('"List item 1"')]),
                    Li([Text('"List item 2"')])
                ]),
                Ol([
                    Li([Text('"Ordered item 1"')]),
                    Li([Text('"Ordered item 2"')])
                ]),
                Hr(),
                Br()
            ])
        ])
        print(html)

    except Exception as exc:
        t_err(str(exc))


# Main
# ----

if __name__ == '__main__':
    try:
        main()
    except Exception as exc:
        print(exc)
