from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse
from django.db import IntegrityError
from django.shortcuts import render, redirect

from .models import *
from .forms import *

def view_populate(request) -> HttpResponse:

    """
    Populate the ex07_movies table in the PostgreSQL
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
        (1, 'The Phantom Menace', 'George Lucas', 'Rick McCallum', '1999-07-19'),
        (2, 'Attack of the Clones', 'George Lucas', 'Rick McCallum', '2002-07-16'),
        (3, 'Revenge of the Sith', 'George Lucas', 'Rick McCallum', '2007-07-19'),
        (4, 'A New Hope', 'George Lucas', 'Gary Kurtz, Rick McCallum', '1977-07-25'),
        (5, 'The Empire Strikes Back', 'Irvin Kershner', 'Gary Kurtz, Rick McCallum', '1980-07-17'),
        (6, 'Return of the Jedi', 'Richard Marquand', 'Howard G. Kazanjian, George Lucas, Rick McCallum', '1983-07-25'),
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
    Display the contents of the ex07_movies table in the
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
        return render(request, 'ex07/display.html', {"movies": movies})
    except Exception as exc:
        messages.info(request, "No data available")
        return render(request, 'ex07/display.html')


def view_remove(request) -> HttpResponse:

    """
    Remove a movie from the ex07_movies table in the
    PostgreSQL database.

    Args:
        request: The HTTP request object.
    
    Returns:
        HttpResponse: The HTTP response object containing
            the result of the operation.
    """

    try:
        if not Movies.fetchall():
            messages.info(request, "No data available")
            return render(request, 'ex07/remove.html')

        if request.method == "POST":
            form = FormMovieDelete(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                Movies.remove(title)
                messages.success(request, f"OK Movie '{title}' removed successfully.")
                return redirect('ex07:remove')
        return render(request, 'ex07/remove.html', {'form': FormMovieDelete()})

    except Exception as e:
        messages.info(request, "No data available")
        return render(request, 'ex07/remove.html')

def view_update(request) -> HttpResponse:

    try:
        if not Movies.fetchall():
            messages.info(request, "No data available")
            return render(request, 'ex07/remove.html')
        if request.method == "POST":
            form = FormMovieUpdate(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                opening_crawl = form.cleaned_data['opening_crawl']
                Movies.update(title, opening_crawl)
                messages.success(request, f"OK Movie '{title}' updated successfully.")
                return redirect('ex07:update')
        return render(request, 'ex07/update.html', {"form": FormMovieUpdate()})
    except Exception as e:
        messages.error(request, f"KO {str(e)}")
        return render(request, 'ex07/remove.html')