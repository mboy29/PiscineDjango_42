
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

from .sources import *

def view_init(request) -> HttpResponse:

    """
    Initialize the ex00_movies table in the 
    PostgreSQL database.

    Args:
        request: The HTTP request object.
    
    Returns:
        HttpResponse: The HTTP response object
            containing the result of the operation.

    Raises:
        Exception: If an error occurs during the 
            database initialization process.
    """

    try:
        with DatabaseManager() as db_manager:
            db_manager.database_table_movies_create()
        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(f"KO {str(e)}")