from django.contrib import admin

from .models import *

# Register your models here.


@admin.register(Planets)
class PlanetsAdmin(admin.ModelAdmin):

    """
    Admin interface configuration for the Planets model.

    This class customizes the Django admin interface for managing Planet records.

    Attributes:
        list_display: Tuple specifying the fields to display in the list view of the admin interface.
            'name': The name of the planet.
            'climate': The climate of the planet.
            'diameter': The diameter of the planet.
            'orbital_period': The orbital period of the planet.
            'population': The population of the planet.
            'rotation_period': The rotation period of the planet.
            'surface_water': The surface water of the planet.
            'terrain': The terrain of the planet.
            'created': The date and time the record was created.
            'updated': The date and time the record was last updated.
        search_fields: Tuple specifying the fields to search for in the admin interface.
            'name': The name of the planet.
            'climate': The climate of the planet.
            'terrain': The terrain of the planet.
    """

    list_display = ('name', 'climate', 'diameter', 'orbital_period', 'population', 'rotation_period', 'surface_water', 'terrain', 'created', 'updated')
    search_fields = ('name', 'climate', 'terrain')

@admin.register(People)
class PeopleAdmin(admin.ModelAdmin):

    """
    Admin interface configuration for the People model.

    This class customizes the Django admin interface for managing People records.

    Attributes:
        list_display: Tuple specifying the fields to display in the list view of the admin interface.
            'name': The name of the person.
            'birth_year': The birth year of the person.
            'gender': The gender of the person.
            'eye_color': The eye color of the person.
            'hair_color': The hair color of the person.
            'height': The height of the person.
            'mass': The mass of the person.
            'homeworld': The homeworld of the person.
            'created': The date and time the record was created.
            'updated': The date and time the record was last updated.
        search_fields: Tuple specifying the fields to search for in the admin interface.
            All fields from list_display are included in search_fields.
    """

    list_display = ('name', 'birth_year', 'gender', 'eye_color', 'hair_color', 'height', 'mass', 'homeworld', 'created', 'updated')
    search_fields = ('name', 'birth_year', 'gender', 'eye_color', 'hair_color', 'height', 'mass', 'homeworld', 'created', 'updated')

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
    readonly_fields: Tuple specifying fields that are read-only in the form.
        'episode_nb': The primary key field, which is read-only because it is auto-generated.

    Methods:
    - __init__: Initializes the MoviesAdmin instance with custom configurations.
    """

    list_display = ('episode_nb', 'title', 'director', 'producer', 'release_date')
    readonly_fields = ('episode_nb',)
