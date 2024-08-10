from django.urls import reverse_lazy
from django.views.generic.base import RedirectView

from app.models import *
from app.forms import *

class ViewHome(RedirectView):
    
    """
    Home page view. Redirects to the articles page.

    Methods:
        get_redirect_url: Determines the URL to redirect to 
            based on the user's authentication status.
    """

    def get_redirect_url(self, *args, **kwargs):
        """
        Determine the redirect URL based on user's authentication status.

        Returns:
            str: URL to redirect to.
        """
        return reverse_lazy('app:articles')
