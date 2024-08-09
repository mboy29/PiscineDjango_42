import random
from datetime import datetime
from django.conf import settings
from django.utils import timezone
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import login, authenticate, logout

from .forms import *
from .models import *
from .sources import *

# Create your views here.

def view_home(request) -> HttpResponse:

    """
    View to render the home page. Handles the display, creation, upvoting,
    downvoting and deletion of tips.

    Args:
        request (HttpRequest): The request object.
    
    Returns:
        HttpResponse: The HTTP response object
    """
   
    try:
        if request.method == 'POST':
            tip_id = request.POST.get('tip_id')
            tip = Tip.fetch(tip_id)
            form = FormTip(request.POST or None)
            if form.is_valid():
                Tip.create(form.cleaned_data['content'], request.user)
                return redirect('ex:home')
            if 'upvote' in request.POST:
                tip.upvote(request.user)
            elif 'downvote' in request.POST:
                tip.downvote(request.user)
            elif 'delete' in request.POST:
                tip.remove(request.user)
            return redirect('ex:home')
    except Exception as e:
        messages.error(request, str(e))
        return redirect('ex:home')
    return render(request, 'home.html', {'user': request.user, 'tips': Tip.fetchall(), 'form': FormTip()})
 
def view_register(request) -> HttpResponse:
    
    """
    Handles the registration of a new user via a form, adds the user 
    to the database, logs then in and updates the session.

    Args:
        request (HttpRequest): The request object.
    
    Returns:
        HttpResponse: The HTTP response object
    """

    try:
        if request.method == 'POST':
            form = FormRegister(request.POST or None)
            if form.is_valid():
                user = form.save(commit=False)
                user.set_password(form.cleaned_data['password'])
                user.save()
                login(request, user)
                with SessionManager(request) as session_manager:
                    session_manager.user_set(user)
                return redirect('ex:home')
            for errors in form.errors.values():
                for error in errors:
                    messages.error(request, error)
            return redirect('ex:register')
    except Exception as e:
        messages.error(e)
        return redirect('ex:register')
    return render(request, 'register.html', {'form': FormRegister()})

def view_login(request) -> HttpResponse:

    """
    Handles the login of a user via a form, authenticates the user,
    logs them in and updates the session.

    Args:
        request (HttpRequest): The request object.
    
    Returns:
        Httpresponse: The HTTP response object
    """

    try:
        if request.method == 'POST':
            form = FormLogin(request.POST or None)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    with SessionManager(request) as session_manager:
                        session_manager.user_set(user)
                    return redirect('ex:home')
            for errors in form.errors.values():
                for error in errors:
                    messages.error(request, error)
            return redirect('ex:login')

    except Exception as e:
        messages.error(e)
        return redirect('ex:login')
    return render(request, 'login.html', {'form': FormLogin()})

def view_logout(request) -> HttpResponse:

    """
    Logs the user out and updates the session.

    Args:
        request (HttpRequest): The request object.
    
    Returns:
        HttpResponse: The HTTP response object
    """

    try:
        logout(request)
        with SessionManager(request) as session_manager:
            session_manager.user_clear()
        return redirect('ex:home')
    except Exception as e:
        messages.error(e)
        return redirect('ex:home')