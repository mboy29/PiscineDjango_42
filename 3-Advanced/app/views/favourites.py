from typing import Any, Dict
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, View
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

        try:
            context = super().get_context_data(**kwargs)
            context['favourites'] = UserFavouriteArticle.fetch(self.request.user)
            return context
        except Exception as e:
            raise Exception(f"Error fetching favourites: {e}")

class AddToFavouritesView(LoginRequiredMixin, View):
    
    """
    View to add an article to favourites.

    Attributes:
        form_class (FormFavourites): The form class to use.

    Methods:
        post: Handles POST requests to add an article to favourites.
    """

    def post(self, request, *args, **kwargs):

        """
        Handles POST requests to add an article to favourites.

        Args:
            request (HttpRequest): The request object.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.      
        
        Returns:
            HttpResponseRedirect: Redirects to the article details page.
        """

        article = get_object_or_404(Article, pk=kwargs['pk'])
        
        form = FormFavourites(request.POST, user=request.user, article=article)
        if form.is_valid():
            UserFavouriteArticle.create(user=request.user, article=article)
            messages.success(request, 'Article added to favourites!')
            return redirect(reverse_lazy('app:favourites'))
        for error in form.non_field_errors():
            messages.error(request, error)
        return redirect(reverse_lazy('app:details', kwargs={'pk': article.pk}))