
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .sources import *
from .forms import *

def view_init(request) -> HttpResponse:

    """
    Initialize the ex06_movies table in the PostgreSQL
    database.

    Args:
        request: The HTTP request object.
    
    Returns:
        HttpResponse: The HTTP response object containing 
            the result of the operation.

    Raises:
        Exception: If an error occurs during the database
            initialization process.
    """


    try:
        with DatabaseManager() as db_manager:
            db_manager.database_table_movies_create()
        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(f"KO {str(e)}")

def view_populate(request) -> HttpResponse:

    """
    Populate the ex06_movies table in the PostgreSQL
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

    db_manager = DatabaseManager()
    data = [
        (1, 'The Phantom Menace', 'George Lucas', 'Rick McCallum', '1999-05-19'),
        (2, 'Attack of the Clones', 'George Lucas', 'Rick McCallum', '2002-05-16'),
        (3, 'Revenge of the Sith', 'George Lucas', 'Rick McCallum', '2005-05-19'),
        (4, 'A New Hope', 'George Lucas', 'Gary Kurtz, Rick McCallum', '1977-05-25'),
        (5, 'The Empire Strikes Back', 'Irvin Kershner', 'Gary Kurtz, Rick McCallum', '1980-05-17'),
        (6, 'Return of the Jedi', 'Richard Marquand', 'Howard G. Kazanjian, George Lucas, Rick McCallum', '1983-05-25'),
        (7, 'The Force Awakens', 'J. J. Abrams', 'Kathleen Kennedy, J. J. Abrams, Bryan Burk', '2015-12-11')
    ]
    results = []
    try:
        with DatabaseManager() as db_manager:
            for record in data:
                try:
                    db_manager.database_table_movies_insert(*record)
                    results.append(f"OK: Movie '{record[1]}' inserted successfully.")
                except psycopg2.IntegrityError as e:
                    db_manager.conn.rollback()
                    results.append(f"KO: Failed to insert '{record[1]}'. IntegrityError: {str(e)}")
                except psycopg2.DatabaseError as e:
                    db_manager.conn.rollback()
                    results.append(f"KO: Failed to insert '{record[1]}'. DatabaseError: {str(e)}")
                except Exception as e:
                    db_manager.conn.rollback()
                    results.append(f"KO: Failed to insert '{record[1]}'. Error: {str(e)}")
    except Exception as e:
        results.append(f"KO: Failed to connect to the database. Error: {str(e)}")
    response = "<br>".join(results)
    return HttpResponse(response)

def view_display(request) -> HttpResponse:

    """
    Display the contents of the ex06_movies table in the
    PostgreSQL database.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object containing
            the result of the operation.

    Raises:
        Exception: If an error occurs during the database
            query process
    """

    try:
        with DatabaseManager() as db_manager:
            movies = db_manager.database_table_movies_get()
            if not movies:
                raise Exception
            return render(request, 'ex06/display.html', {"movies": movies})
    except Exception as exc:
        messages.info(request, "No data available")
        return render(request, 'ex06/display.html')

def view_remove(request) -> HttpResponse:

    """
    Displays and processes a form to remove movies from the 
    ex06_movies table. This view displays a form for removing a 
    movie if movies are available.
    
    If the form is submitted and valid, it removes the selected movie 
    and displays a success message. If no movies are available or an 
    error occurs, it displays an appropriate message.

    Args:
        request: The HTTP request object.
    
    Returns:
        HttpResponse: The HTTP response object containing
            the result of the operation.
    """
    
    try:
        with DatabaseManager() as db_manager:
            if not db_manager.database_table_movies_get():
                messages.info(request, "No data available")
                return render(request, 'ex06/remove.html')
            if request.method == "POST":
                form = FormMovieDelete(request.POST)
                if form.is_valid():
                    title = form.cleaned_data['title']
                    db_manager.database_table_movie_delete(title)
                    messages.success(request, f"OK Movie '{title}' removed successfully.")
                    return redirect('ex06:remove')
            return render(request, 'ex06/remove.html', {"form": FormMovieDelete()})

    except Exception as e:
        messages.info(request, "No data available")
        return render(request, 'ex06/remove.html')

def view_update(request) -> HttpResponse:

    """
    Displays and processes a form to update the opening crawl
    of a movie in the ex06_movies table. This view displays a form
    for updating a movie if movies are available.

    If the form is submitted and valid, it updates the opening crawl
    of the selected movie and displays a success message. If no movies
    are available or an error occurs, it displays an appropriate message.

    Args:
        request: The HTTP request object.
    
    Returns: 
        HttpResponse: The HTTP response object containing
            the result of the operation.
    """

    try:
        with DatabaseManager() as db_manager:
            if not db_manager.database_table_movies_get():
                messages.info(request, "No data available")
                return render(request, 'ex06/update.html')
            if request.method == "POST":
                form = FormMovieUpdate(request.POST)
                if form.is_valid():
                    title = form.cleaned_data['title']
                    opening_crawl = form.cleaned_data['opening_crawl']
                    db_manager.database_table_movies_update(title, opening_crawl)
                    messages.success(request, f"OK Movie '{title}' updated successfully.")
                    return redirect('ex06:update')
        return render(request, 'ex06/update.html', {"form": FormMovieUpdate()})

    except Exception as e:
        messages.error(request, f"KO {str(e)}")
        return redirect('update')
