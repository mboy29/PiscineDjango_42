
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

from .sources import *
from .forms import *

def view_init(request) -> HttpResponse:

    """
    Initialize the ex02_movies table in the PostgreSQL
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
    Populate the ex02_movies table in the PostgreSQL
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
    Display the contents of the ex02_movies table in the
    PostgreSQL database.

    Args:
        request: The HTTP request object.
    
    Returns:
        HttpResponse: The HTTP response object containing
            the result of the operation.
    """

    try:
        with DatabaseManager() as db_manager:
            rows = db_manager.database_table_movies_get()
            context = {'rows': rows} if rows else {'message': "No data available"}
            return render(request, 'ex02/display.html', context)
    except Exception as exc:
        return render(request, 'ex02/display.html', {'message': "No data available"})

def view_remove(request, *args, **kwargs) -> HttpResponse:

    """
    Displays and processes a form to remove movies from the 
    ex04_movies table. This view displays a form for removing a 
    movie if movies are available.
    
    If the form is submitted and valid, it removes the selected movie 
    and displays a success message. If no movies are available or an 
    error occurs, it displays an appropriate message.

    Args:
        request: The HTTP request object.
        kwargs: A dictionary containing additional keyword arguments.
    
    Returns:
        HttpResponse: The HTTP response object containing
            the result of the operation.
    """

    context = {}
    if 'success' in kwargs:
        context['success'] = kwargs['success']
    
    try:
        with DatabaseManager() as db_manager:
            movies = db_manager.database_table_movies_get()
            if not movies:
                context['message'] = "No data available"
                return render(request, 'ex04/remove.html', context)
            if request.method == "POST":
                form = FormMovieDelete(request.POST)
                if form.is_valid():
                    title = form.cleaned_data['title']
                    db_manager.database_table_movie_delete(title)
                    return view_remove(request, success=f"Movie '{title}' removed successfully.")
            context['form'] = FormMovieDelete()
            return render(request, 'ex04/remove.html', context)

    except Exception as e:
        context['message'] = "No data available"
        return render(request, 'ex04/remove.html', context)