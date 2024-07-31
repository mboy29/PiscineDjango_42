from django.contrib import admin
from .models import Movies

@admin.register(Movies)
class MoviesAdmin(admin.ModelAdmin):
    """
    Admin interface configuration for the Movies model.

    This class customizes the Django admin interface for managing Movie records.
    
    Attributes:
        list_display: Tuple specifying the fields to display in the list view of the admin interface.
            'episode_nb': The primary key and auto-incrementing field.
            'title': The title of the movie.
            'director': The director of the movie.
            'producer': The producer of the movie.
            'release_date': The release date of the movie.
        fields: Tuple specifying the fields to display on the form for adding or editing a Movie.
            'title': The title of the movie.
            'episode_nb': The primary key of the movie (read-only).
            'opening_crawl': The opening crawl text of the movie.
            'director': The director of the movie.
            'producer': The producer of the movie.
            'release_date': The release date of the movie.
    readonly_fields: Tuple specifying fields that are read-only in the form.
        'episode_nb': The primary key field, which is read-only because it is auto-generated.

    Methods:
    - __init__: Initializes the MoviesAdmin instance with custom configurations.
    """

    list_display = ('episode_nb', 'title', 'director', 'producer', 'release_date')
    fields = ('title', 'episode_nb', 'opening_crawl', 'director', 'producer', 'release_date')
    readonly_fields = ('episode_nb',)
