
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse
from django.db import IntegrityError, transaction

from .models import *

def view_populate(request) -> HttpResponse:

    """
    Populate the ex03_movies table in the PostgreSQL
    database with data.

    Args: 
        request: The HTTP request object.
    
    Returns:
        HttpResponse: The HTTP response object containing
            the result of the operation.
    
    Raises:
        Exception: If an error occurs during the database
            population process.
    """

    data = [
        (1, 'The Phantom Menace', 'George Lucas', 'Rick McCallum', '1999-05-19'),
        (2, 'Attack of the Clones', 'George Lucas', 'Rick McCallum', '2002-05-16'),
        (3, 'Revenge of the Sith', 'George Lucas', 'Rick McCallum', '2005-05-19'),
        (4, 'A New Hope', 'George Lucas', 'Gary Kurtz, Rick McCallum', '1977-05-25'),
        (5, 'The Empire Strikes Back', 'Irvin Kershner', 'Gary Kurtz, Rick McCallum', '1980-05-17'),
        (6, 'Return of the Jedi', 'Richard Marquand', 'Howard G. Kazanjian, George Lucas, Rick McCallum', '1983-05-25'),
        (7, 'The Force Awakens', 'J. J. Abrams', 'Kathleen Kennedy, J. J. Abrams, Bryan Burk', '2015-12-11'),
    ]

    results = []
    for record in data:
        try:
            result = Movies.insert(*record)
            results.append(f"OK {result}")
        except IntegrityError as exc:
            results.append(f"KO {exc}")
        except Exception as e:
            results.append(f"KO {e}")
    response = "<br>".join(results)
    return HttpResponse(response)


def view_display(request) -> HttpResponse:

    """
    Display the contents of the ex03_movies table in the
    PostgreSQL database.

    Args:
        request: The HTTP request object.
    
    Returns:
        HttpResponse: The HTTP response object containing
            the result of the operation.
    """

    try:
        movies = Movies.fetchall()
        if not movies:
            raise Exception
        return render(request, 'ex03/display.html', {"movies": movies})
    except Exception as exc:
        messages.info(request, "No data available")
        return render(request, 'ex03/display.html')