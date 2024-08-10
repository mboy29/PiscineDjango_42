from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404
from django.utils.translation import gettext_lazy as _

from app.models import *
from app.forms import *

class ViewDetails(DetailView):
    
    """
    Detail view for a single article.

    Attributes:
        model (Article): The model to use.
        template_name (str): Template file to render.
        context_object_name (str): Context name for the article.
    """
    
    model = Article
    template_name = 'details.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = FormFavourites(user=self.request.user, article=self.get_object())
        return context
    
    def get_object(self):
        """
        Fetch the article based on the ID from the URL.
        
        Returns:
            Article: The article object if found, otherwise raises a 404 error.
        """
        article_id = self.kwargs.get('pk')
        return get_object_or_404(Article, pk=article_id)
