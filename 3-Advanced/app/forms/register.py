from django import forms
from app.models import *

class FormRegister(forms.ModelForm):
    
    """
    Form class to register a new user.

    Feilds:
        username (str): The username.
        password (str): The password.
        password_confirmation (str): The password confirmation.
    
    Methods:
        clean(): Validates the form fields.
        save(commit=True): Saves the form data to the database.
    """
    
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput(), max_length=128, required=True)
    password_confirmation = forms.CharField(widget=forms.PasswordInput(), max_length=128, required=True)

    class Meta:

        """
        The model meta class for the FormRegister class.

        Attributes:
            model (User): The model to use.
            fields (list): The fields to include in the form.
            widgets (dict): The widgets to use for the fields.
        """

        model = User
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean(self):

        """
        Validates the form fields, by checking if the username already
        exists and if the passwords match.

        Args: None

        Returns:
            dict: The cleaned data.
        """

        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        password_confirmation = cleaned_data.get('password_confirmation')

        if User.objects.filter(username=username).exists():
            self.add_error("username", 'Username already exists.')
        elif password != password_confirmation:
            self.add_error("password", 'Passwords do not match.')
        return cleaned_data