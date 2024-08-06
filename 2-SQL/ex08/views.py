import os
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .sources import *

# Create your views here.

def view_init(request) -> HttpResponse:

    """
    Renders the init page and initializes the planets and 
    people tables.

    Args:
        request: The request object.
    
    Returns:
        HttpResponse: The HTTP response.
    """

    def view_init_planets():

        """
        Initializes the planets table.

        Args: None

        Returns: None

        Raises:
            Exception: If an error occurs.
        """

        try:
            with DatabaseManager() as db_manager:
                db_manager.planets_init()
                messages.success(request, "OK Table planets successfully created")
        except Exception as e:
            messages.error(request, f"KO {str(e)}")
    
    def view_init_people():

        """
        Initializes the people table.

        Args: None

        Returns: None

        Raises:
            Exception: If an error occurs.
        """

        try:
            with DatabaseManager() as db_manager:
                db_manager.people_init()
                messages.success(request, "OK Table people successfully created")
        except Exception as e:
            messages.error(request, f"KO {str(e)}")
        
    try:
        view_init_planets()
        view_init_people()
    except Exception as e:
        messages.error(request, f"KO {str(e)}")
    return render(request, 'ex08/init.html')

def view_populate(request) -> HttpResponse:
    
    """
    Renders the populate page and populates the planets and
    people tables with data from 2 different CSV files.

    Args:
        request: The request object.
        
    Returns:
        HttpResponse: The HTTP response.
    
    Raises:
        Exception: If an error occurs
    """

    def view_populate_planets():
        
        """
        Populates the planets table by reading data from a CSV file
        and inserting it into the table using copy_from.

        Args: None

        Returns: None

        Raises:
            Exception: If an error occurs.
        """
        
        file_path = os.path.join(settings.BASE_DIR, 'ex08/data/planets.csv')
        try:
            with DatabaseManager() as db_manager:
                db_manager.planets_insert(file_path)
            messages.success(request, "OK populating planets table")
                   
        except Exception as e:
            messages.error(request, f"KO {str(e)}")
    
    def view_populate_people():
        
        """
        Populates the people table by reading data from a CSV file
        and inserting it into the table using copy_from.

        Args: None

        Returns: None
        """
        
        file_path = os.path.join(settings.BASE_DIR, 'ex08/data/people.csv')
        try:
            with DatabaseManager() as db_manager:
                db_manager.people_insert(file_path)
            messages.success(request, "OK populating people table")
        except Exception as e:
            messages.error(request, f"KO {str(e)}")

    try:
        view_populate_planets()
        view_populate_people()
    except Exception as e:
        messages.error(request, f"KO {str(e)}")
    return render(request, 'ex08/populate.html')

def view_display(request) -> HttpResponse:

    """
    Displays the data from the people table, and renders the display page.
    It specifically displays the characters' names, their homeworld, and 
    the climate of their homeworld where the climate is windy or moderately
    windy, sorted alphabetically by the homeworld's name.

    Args:
        request: The request object.
    
    Returns:
        HttpResponse: The HTTP response.
    """

    try:
        with DatabaseManager() as db_manager:
            data = db_manager.people_get()
            if not data:
                raise Exception;
            return render(request, 'ex08/display.html', {'data': data})
    except Exception as e:
        messages.error(request, "No data available")
        return render(request, 'ex08/display.html')
