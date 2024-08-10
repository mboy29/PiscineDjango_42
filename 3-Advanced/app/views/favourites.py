from typing import Any, Dict
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.base import RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect

from app.models import *
from app.forms import *

class ViewFavourites(ListView):

    """
    Articles page view. Displays all articles.

    attributes:
        template_name (str): Template file to render.
        model (Article): Model to use for fetching data.
        queryset (QuerySet): Queryset to fetch data.
    
    Methods:
        get_context_data: Creates the context 
            for the template.
    """

    template_name = "favourites.html"
    model = Article
    queryset = Article.objects.filter().order_by('-created')

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        
        """
        Creates the context for the template.

        Args:
            **kwargs: Arbitrary keyword arguments.
        
        Returns:
            Dict[str, Any]: Context for the template.
        """

        context = super().get_context_data(**kwargs)
        context['favourites'] = UserFavouriteArticle.fetch(self.request.user)
        return context

class AddToFavouritesView(LoginRequiredMixin, RedirectView):

    """
    Add to favourites view. Adds an article to the user's favourites.

    attributes:
        pattern_name (str): URL pattern name.
        permanent (bool): Permanent redirect flag.
    
    Methods:
        get_redirect_url: Redirects to the favourites page.
    """
    permanent = False

    def get_redirect_url(self, *args, **kwargs):

        """
        Redirects to the favourites page.

        Args:
            *args: Arbitrary positional arguments.
            **kwargs: Arbitrary keyword arguments.
        
        Returns:
            str: URL to redirect to.
        """

        article = get_object_or_404(Article, pk=kwargs['pk'])
        
        if not UserFavouriteArticle.exists(self.request.user, article):
            UserFavouriteArticle.create(user=self.request.user, article=article)
        return reverse_lazy('app:favourites')