from typing import Any, Dict
from django.urls import reverse_lazy
from django.views.generic.list import ListView

from app.models import *
from app.forms import *

class ViewArticles(ListView):

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

    template_name = "articles.html"
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
        context['articles'] = Article.fetchall()
        return context