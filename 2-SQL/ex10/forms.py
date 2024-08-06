from django import forms
from django.db.models import Min, Max

from .models import *

class FormSearch(forms.Form):

    """
    Form to handle the search functionality for movies.

    Attributes:
        min_release_date (DateField): The minimum release date of the movies.
        max_release_date (DateField): The maximum release date of the movies.
        min_diameter (IntegerField): The minimum diameter of the planets.
        gender (Choice): The gender of the characters in the movies.
    
    Methods:
        __init__: Initializes the form with the minimum and maximum release
            dates, the minimum diameter of the planets, and the character's
    """

    min_release_date = forms.DateField(label='Movies minimum release date', widget=forms.SelectDateWidget())
    max_release_date = forms.DateField(label='Movies maximum release date', widget=forms.SelectDateWidget())
    min_diameter = forms.IntegerField(label='Planet diameter greater than')
    gender = forms.ChoiceField(label='Character gender', choices=[])

    def __init__(self, *args, **kwargs):

        """
        Initializes the form with the minimum and maximum release dates, the
        minimum diameter of the planets, and the character's gender based on
        the data in the database.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        
        Returns: None
        """

        super().__init__(*args, **kwargs)
        oldest_date = Movies.objects.aggregate(Min('release_date'))['release_date__min']
        latest_date = Movies.objects.aggregate(Max('release_date'))['release_date__max']
        if oldest_date and latest_date:
            min_year = oldest_date.year
            max_year = latest_date.year
            self.fields['min_release_date'].widget = forms.SelectDateWidget(years=range(min_year, max_year + 1))
            self.fields['max_release_date'].widget = forms.SelectDateWidget(years=range(min_year, max_year + 1))

        genders = People.objects.values_list('gender', flat=True).distinct()
        self.fields['gender'].choices = [(gender, gender) for gender in genders if gender]
