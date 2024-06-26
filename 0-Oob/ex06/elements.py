# Imports
# -------
from elem import *

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
