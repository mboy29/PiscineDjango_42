from django import forms
from .models import *

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
    
    username = forms.CharField(max_length=150, help_text="Enter a username.", required=True)
    password = forms.CharField(widget=forms.PasswordInput(), max_length=128, help_text="Enter your password.", required=True)
    password_confirmation = forms.CharField(widget=forms.PasswordInput(), max_length=128, help_text="Enter the same password again for verification.", required=True)

    class Meta:
        model = CustomUser
        fields = ['username']

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

        if CustomUser.objects.filter(username=username).exists():
            self.add_error("username", 'Username already exists.')
        elif password != password_confirmation:
            self.add_error("password", 'Passwords do not match.')
        return cleaned_data

    def save(self, commit=True):

        """
        Saves the form data to the database.

        Args:
            commit (bool): The commit flag.

        Returns:
            CustomUser: The user object.
        """

        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        if commit:
            user = CustomUser.create(username=username, password=password)
        else:
            user = CustomUser(username=username)
            user.set_password(password)
        return user


class FormLogin(forms.Form):

    """
    Form class to login a user.

    Feilds:
        username (str): The username.
        password (str): The password.
    
    Methods:
        clean(): Validates the form fields.
    """

    username = forms.CharField(max_length=150, help_text="Enter your username.", required=True)
    password = forms.CharField(widget=forms.PasswordInput(), max_length=128, help_text="Enter your password.", required=True)

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

        if not CustomUser.exists(username):
            self.add_error("username", 'Username does not exist.')
        else:
            user = CustomUser.fetch(username)
            if not user.check_password(password):
                self.add_error("password", 'Incorrect password.')
        return cleaned_data

class FormTip(forms.ModelForm):

    """
    Form class to create a new tip.  

    Feilds:
        content (str): The tip content.
    
    Methods:
        save(commit=True): Saves the form data to the database.
    """
    
    class Meta:
        model = Tip
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3}),
        }