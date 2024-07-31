from django import forms
from .sources import *

class FormMovieDelete(forms.Form):
    
    """
    A Django form for selecting and removing a movie from the database.

    Attributes:
        title (forms.ChoiceField): A dropdown field to select a movie from the list.
    
    Methods:
        __init__: Initializes the form and populates the choices for the title field.
        form_movies_delete_get: Retrieve movie titles from the database to populate the dropdown choices.
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
        self.fields['title'].choices = self.form_movies_delete_get()

    def form_movies_delete_get(self):
        
        """
        Retrieve movie titles from the database to populate the dropdown choices.

        Args:
            None

        Returns:
            list: A list of tuples where each tuple contains (value, display) for the dropdown options.
                  Returns an empty list if no movies are found.
        """
        
        with DatabaseManager() as db_manager:
            movies = db_manager.database_table_movies_get()
            if not movies:
                return []
            return [(movie[1], movie[1]) for movie in movies]

