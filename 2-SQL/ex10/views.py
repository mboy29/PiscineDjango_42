from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse
from django.db import IntegrityError
from django.shortcuts import render, redirect

from .models import *
from .forms import *

# Create your views here.

def view_search(request) -> HttpResponse:
    
    """
    Handles the search functionality and renders the appropriate response.
    The search allows users to filter movies based on the release date,
    characters, characters' homeworlds, and characters' homeworlds' diameter.

    Args:
        request (HttpRequest): The request object sent by the client.
    
    Returns:
        HttpResponse: The response object that contains the rendered
            template with the search form and search results.s
    """

    try:
        form = FormSearch(request.GET or None)
        data = []
        if request.method == 'GET' and form.is_valid():
            kwargs = {
                'min_release_date': form.cleaned_data.get('min_release_date'),
                'max_release_date': form.cleaned_data.get('max_release_date'),
                'min_diameter': form.cleaned_data.get('min_diameter'),
                'gender': form.cleaned_data.get('gender'),
            }

            results = Movies.fetchall(**kwargs)
            data = [" - ".join(map(str, result)) for result in results]
            
            if not results:
                messages.error(request, 'Nothing corresponding to your research.')
                return redirect('ex10:search')
            request.session['search_results'] = data
            return redirect('ex10:search')

    except Exception as e:
        messages.error(request, str(e))
    data = request.session.get('search_results', [])
    request.session.pop('search_results', None)
    return render(request, 'ex10/search.html', {'form': FormSearch(), 'data': data})