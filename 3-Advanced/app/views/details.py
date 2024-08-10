from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404

from app.models import Article

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

    def get_object(self):
        """
        Fetch the article based on the ID from the URL.
        """
        article_id = self.kwargs.get('pk')
        return get_object_or_404(Article, pk=article_id)
