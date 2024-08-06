from django import forms

from .models import *

class FormMovieDelete(forms.Form):
    
    """
    A Django form for selecting and removing a movie from the database.

    Attributes:
        title (forms.ChoiceField): A dropdown field to select a movie from the list.
    
    Methods:
        __init__: Initializes the form and populates the choices for the title field.
        fetchall: Retrieve movie titles from the database to populate the dropdown choices.
    """

    title = forms.ChoiceField(label="Select Movie to Remove")

    def __init__(self, *args, **kwargs):
       
        """
        Initialize the form and populate the choices for the title field.

        Args:
            *args: Variable length argument list for form initialization.
            **kwargs: Keyword arguments for form initialization. Typically includes POST data and files.

        Updates:
            Populates the 'title' field with choices from the database.
        """
        
        super(FormMovieDelete, self).__init__(*args, **kwargs)
        self.fields['title'].choices = self.fetchall()

    def fetchall(self):
        
        """
        Retrieve movie titles from the database to populate the dropdown choices.

        Args:
            None

        Returns:
            list: A list of tuples where each tuple contains (value, display) for the dropdown options.
                  Returns an empty list if no movies are found.
        """
        
        try:
            movies = Movies.fetchall()
            if not movies:
                return []
            return [(movie[1], movie[1]) for movie in movies]
        except Exception as e:
            return []

class FormMovieUpdate(forms.Form):

    """
    A Django form for selecting a movie and updating its opening crawl
    in the database. 

    Attributes:
        title (forms.ChoiceField): A dropdown field to select a movie from the list.
        opening_crawl (forms.CharField): A textarea field to enter the new opening crawl.
    
    Methods:
        __init__: Initializes the form and populates the choices for the title field.
        fetchall: Retrieve movie titles from the database to populate the dropdown choices
    """

    title = forms.ChoiceField(choices=[], label="Select Movie")
    opening_crawl = forms.CharField(widget=forms.Textarea, label="New Opening Crawl", required=True)

    def __init__(self, *args, **kwargs):

        """
        Initialize the form and populate the choices for the title field.

        Args:
            *args: Variable length argument list for form initialization.
            **kwargs: Keyword arguments for form initialization. Typically includes POST data and files.

        Updates:
            Populates the 'title' field with choices from the database.
        """

        super(FormMovieUpdate, self).__init__(*args, **kwargs)
        self.fields['title'].choices = self.fetchall()
    
    def fetchall(self):
        
        """
        Retrieve movie titles from the database to populate the dropdown choices.

        Args:
            None

        Returns:
            list: A list of tuples where each tuple contains (value, display) for the dropdown options.
                  Returns an empty list if no movies are found.
        """
        
        try:
            movies = Movies.fetchall()
            if not movies:
                return []
            return [(movie[1], movie[1]) for movie in movies]
        except Exception as e:
            return []