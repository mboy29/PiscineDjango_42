from django import forms

from app.models import *

class FormFavourites(forms.ModelForm):

    """
    Form to add an article to the user's favourites.

    Attributes:
        user (User): The user.
        article (Article): The article.
    """

    class Meta:
        model = UserFavouriteArticle
        fields = []

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.article = kwargs.pop('article')
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        if UserFavouriteArticle.exists(self.user, self.article):
            raise forms.ValidationError("Article already in favourites")
        return cleaned_data
    
