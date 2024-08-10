from django import forms
from django.utils.translation import gettext as _
from app.models import *

class FormLogin(forms.Form):
    
    """
    Form class to login a user.

    Fields:
        username (str): The username.
        password (str): The password.
    
    Methods:
        clean(): Validates the form fields.
    """

    username = forms.CharField(
        max_length=150, 
        required=True, 
        widget=forms.TextInput(attrs={'placeholder': _('Username'), 'class': 'form-control'})
    )
    password = forms.CharField(
        max_length=128, 
        required=True, 
        widget=forms.PasswordInput(attrs={'placeholder': _('Password'), 'class': 'form-control'})
    )

    class Meta:
        
        """
        The model meta class for the FormLogin class.

        Attributes:
            model (User): The model to use.
            fields (list): The fields to include in the form.
            widgets (dict): The widgets to use for the fields.
            labels (dict): The labels for the fields.
            help_texts (dict): The help texts for the fields
        """

        model = User
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
        labels = {
            'username': _('Username'),
            'password': _('Password'),
        }
        error_messages = {
            'username': {
                'max_length': _('Username is too long.'),
                'required': _('Username is required.'),
            },
            'password': {
                'max_length': _('Password is too long.'),
                'required': _('Password is required.'),
            },
        }

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
            self.add_error("username", _('Username does not exist.'))
        else:
            user = User.fetch(username)
            if not user.check_password(password):
                self.add_error("password", _('Incorrect password.'))
        return cleaned_data
