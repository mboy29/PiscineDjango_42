from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def view_django(request) -> HttpResponse:

    """
    Display the Django page.

    Args:
        request (HttpRequest): the request object.
    
    Returns:
        HttpResponse: the response object.
    """

    return render(request, 'ex01/django.html')

def view_display(request) -> HttpResponse:

    """
    Display the Display page.

    Args:
        request (HttpRequest): the request object.
    
    Returns:
        HttpResponse: the response object.
    """

    return render(request, 'ex01/display.html')

def view_templates(request) -> HttpResponse:

    """
    Display the Templates page.

    Args:
        request (HttpRequest): the request object.
    
    Returns:
        HttpResponse: the response object.
    """

    return render(request, 'ex01/templates.html')
