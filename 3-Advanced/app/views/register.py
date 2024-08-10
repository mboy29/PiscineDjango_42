from typing import Any, Dict
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.http import HttpResponse
from django.contrib.auth import login as authenticate_login
from django.contrib import messages

from app.models import User
from app.forms import FormRegister

class ViewRegister(FormView):

    """
    Registration page view. Displays the registration form and handles 
    user registration.

    Attributes:
        template_name (str): Template file to render.
        form_class (FormRegister): Form class to use.
        success_url (str): URL to redirect to on success.
    
    Methods:
        form_valid: Handle the form submission when the 
            form is valid.
        form_invalid: Handle the form submission when the
            form is invalid.
    """

    template_name = 'register.html'
    form_class = FormRegister
    success_url = reverse_lazy('app:articles')  # Redirect to login page on successful registration

    def form_valid(self, form) -> HttpResponse:

        """
        Handle the form submission when the form is valid.
        Create a new user and log them in.
        
        Args:
            form (FormRegister): Form instance.
        
        Returns:
            HttpResponse: Redirect to the success URL.
        """

        # Extract the cleaned data from the form
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        # Create a new user
        user = User.objects.create_user(username=username, password=password)
        user.save()

        # Automatically log the user in after registration
        authenticate_login(self.request, user)

        return super().form_valid(form)

    def form_invalid(self, form) -> HttpResponse:

        """
        Handle the form submission when the form is invalid.
        
        Args:
            form (FormRegister): Form instance.

        Returns:
            HttpResponse: Render the form with errors.
        """

        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)
