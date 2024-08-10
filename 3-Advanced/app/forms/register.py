from django import forms
from django.utils.translation import gettext_lazy as _

from app.models import User

class FormRegister(forms.ModelForm):
    
    """
    Form class to register a new user.

    Fields:
        username (str): The username.
        password (str): The password.
        password_confirmation (str): The password confirmation.
    
    Methods:
        clean(): Validates the form fields.
        save(commit=True): Saves the form data to the database.
    """
    
    username = forms.CharField(max_length=150,  required=True, label=_('Username'))
    password = forms.CharField( widget=forms.PasswordInput(),  max_length=128,  required=True, label=_('Password'))
    password_confirmation = forms.CharField(widget=forms.PasswordInput(), max_length=128, required=True, label=_('Confirm Password'))

    class Meta:
        
        """
        The model meta class for the FormRegister class.

        Attributes:
            model (User): The model to use.
            fields (list): The fields to include in the form.
            widgets (dict): The widgets to use for the fields.
            labels (dict): The labels for the fields.
            help_texts (dict): The help texts for the fields.
        """

        model = User
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
        labels = {
            'username': _('Username'),
            'password': _('Password'),
            'password_confirmation': _('Confirm Password'),
        }
        help_texts = {
            'username': _('Enter a unique username.'),
            'password': _('Enter a password.'),
            'password_confirmation': _('Confirm the password.'),
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
            'password_confirmation': {
                'max_length': _('Password is too long.'),
                'required': _('Password is required.'),
            },
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
            self.add_error("username", _('Username already exists.'))
        elif password != password_confirmation:
            self.add_error("password", _('Passwords do not match.'))
        return cleaned_data
