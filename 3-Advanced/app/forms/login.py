from django import forms
from app.models import *

class FormLogin(forms.Form):

    """
    Form class to login a user.

    Feilds:
        username (str): The username.
        password (str): The password.
    
    Methods:
        clean(): Validates the form fields.
    """

    username = forms.CharField(
        max_length=150, 
        required=True, 
        widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'})
    )
    password = forms.CharField(
        max_length=128, 
        required=True, 
        widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'})
    )

    def clean(self):

        """
        Validates the form fields, by checking if the username exists
        and if the password is correct.

        Args: None

        Returns:
            dict: The cleaned data.
        """

        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if not User.exists(username):
            self.add_error("username", 'Username does not exist.')
        else:
            user = User.fetch(username)
            if not user.check_password(password):
                self.add_error("password", 'Incorrect password.')
        return cleaned_data