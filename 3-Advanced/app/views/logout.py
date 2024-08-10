from django.shortcuts import redirect
from django.contrib.auth import logout as auth_logout
from django.views import View
from django.urls import reverse_lazy

class ViewLogout(View):
    
    """
    Custom Logout view that logs out the user and redirects them to the home page.
    """

    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return redirect(reverse_lazy('app:home'))