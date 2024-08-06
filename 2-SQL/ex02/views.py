from django.conf import settings
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse

from .sources import *

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

    Raises:
        Exception: If an error occurs during the database
            query process
    """

    try:
        with DatabaseManager() as db_manager:
            movies = db_manager.database_table_movies_get()
            if not movies:
                raise Exception
            return render(request, 'ex02/display.html', {"movies": movies})
    except Exception as exc:
        messages.info(request, "No data available")
        return render(request, 'ex02/display.html')