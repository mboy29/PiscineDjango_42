from django import forms

from app.models import *

class FormArticle(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'synopsis', 'content']  # Exclude 'author'
