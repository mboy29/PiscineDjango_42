import logging
from datetime import datetime
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import *
from .sources import *

# LOGGER
# ------

def view_index(request) -> HttpResponse:

    """
    Display the form and the history of inputs.

    Args:
        request (HttpRequest): the request object.
    
    Returns:
        HttpResponse: the response object.
    """

    if request.method == 'POST':
        form = FormInput(request.POST)
        if form.is_valid():
            logger_update(form.cleaned_data['field_input'])
        return redirect('form')
    return render(request, 'ex02/index.html', {
        'form': FormInput(), 
        'history': logger_read()
    })
