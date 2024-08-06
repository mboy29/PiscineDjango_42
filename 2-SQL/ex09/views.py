from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse
from django.db import IntegrityError
from django.shortcuts import render, redirect

from .models import *

# Create your views here.

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
        data = People.fetchall()
        if not data:
            raise Exception
        return render(request, 'ex09/display.html', {"data": data})
    except Exception as e:
        messages.warning(request, "No data available, please use the following command line before use: python3 -B manage.py ex09_populate or python -B manage.py loaddata ex09/data/ex09_initial_data.json")
        messages.warning(request, "Then, rerun the server using: python3 -B manage.py runserver or make django_run")
        return render(request, 'ex09/display.html')