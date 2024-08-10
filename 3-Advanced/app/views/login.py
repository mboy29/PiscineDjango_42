from typing import Any, Dict
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic.edit import FormView
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login as authenticate_login

from app.models import *
from app.forms import *

class ViewLogin(FormView):

    """
    Login page view. Displays the login form.

    Attributes:
        template_name (str): Template file to render.
        form_class (FormLogin): Form class to use.
        success_url (str): URL to redirect to on success.
    
    Methods:
        form_valid: Handle the form submission when the 
            form is valid.
        form_invalid: Handle the form submission when the
            form is invalid.
    """

    template_name = 'login.html'
    form_class = FormLogin
    success_url = reverse_lazy('app:articles')

    def form_valid(self, form) -> HttpResponse:
        
        """
        Handle the form submission when the form is valid.
        Authenticate the user and log them in.
        
        Args:
            form (FormLogin): Form instance.
        
        Returns:
            HttpResponse: Redirect to the success URL.
        """
        
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            authenticate_login(self.request, user)
            return super().form_valid(form)
        return self.form_invalid(form)

    def form_invalid(self, form) -> HttpResponse:
        
        """
        Handle the form submission when the form is invalid.
        
        Args:
            form (FormLogin): Form instance.

        Returns:
            HttpResponse: Render the form with errors.
        """
        
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

class ViewLoginNav(FormView):

    """
    Login page view. Displays the login form in the nav bar

    Attributes:
        template_name (str): Template file to render.
        form_class (FormLogin): Form class to use.
        success_url (str): URL to redirect to on success.
    
    Methods:
        form_valid: Handle the form submission when the 
            form is valid.
        form_invalid: Handle the form submission when the
            form is invalid.
    """

    template_name = 'nav.html'
    form_class = FormLogin
    success_url = reverse_lazy('app:articles')

    def form_valid(self, form) -> HttpResponse:
        
        """
        Handle the form submission when the form is valid.
        Authenticate the user and log them in.
        
        Args:
            form (FormLogin): Form instance.
        
        Returns:
            HttpResponse: Redirect to the success URL.
        """
        
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            authenticate_login(self.request, user)
            return super().form_valid(form)
        return self.form_invalid(form)

    def form_invalid(self, form) -> HttpResponse:
        
        """
        Handle the form submission when the form is invalid.
        
        Args:
            form (FormLogin): Form instance.

        Returns:
            HttpResponse: Render the form with errors.
        """
        
        referer_url = self.request.META.get('HTTP_REFERER', '/')
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return redirect(referer_url)