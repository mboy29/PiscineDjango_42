from django import forms
from django.utils.translation import gettext_lazy as _

from app.models import *

class FormArticle(forms.ModelForm):

    """
    Form class to publish an article.

    Fields:
        title (str): The title of the article.
        synopsis (str): The synopsis of the article.
        content (str): The content of the article.
    
    Methods: None
    """
    
    class Meta:

        """
        The model meta class for the FormArticle class.

        Attributes:
            model (Article): The model to use.
            fields (list): The fields to include in the form.
            labels (dict): The labels for the fields.
            help_texts (dict): The help texts for the fields.
            error_messages (dict): The error messages for the fields.
        """

        model = Article
        fields = ['title', 'synopsis', 'content']  # Exclude 'author'
        labels = {
            'title': _('Title'),
            'synopsis': _('Synopsis'),
            'content': _('Content'),
        }
        help_texts = {
            'title': _('Enter the title of the article.'),
            'synopsis': _('Provide a brief summary of the article.'),
            'content': _('Write the full content of the article.'),
        }
        error_messages = {
            'title': {
                'required': _('This field is required.'),
                'max_length': _('Title is too long.'),
            },
            'synopsis': {
                'required': _('This field is required.'),
            },
            'content': {
                'required': _('This field is required.'),
            },
        }
