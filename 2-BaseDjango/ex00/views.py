from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def view_index(request) -> HttpResponse:

    """
    Display the index page.

    Args:
        request (HttpRequest): the request object.
    
    Returns:
        HttpResponse: the response object.
    """

    return render(request, 'index.html', {})