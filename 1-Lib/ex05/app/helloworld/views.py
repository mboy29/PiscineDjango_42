# IMPORTS
# -------

from django.shortcuts import render
from django.http import HttpResponse


# VIEWS
# -----

# Create your views here.

def hello_world(request):
    
    """
    View that returns a simple HTTP response containing 
    the text "Hello World!" as required by the exercise.

    Parameters:
        - request: HttpRequest object
    
    Returns: 
        - HttpResponse object containing the text 
            "Hello World!"
    """
    
    return HttpResponse("Hello World!")