from django import forms

from app.models import *

class FormFavouritesAdd(forms.ModelForm):
    class Meta:
        model = UserFavouriteArticle
        fields = []
