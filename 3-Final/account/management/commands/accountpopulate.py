from django.core.management.base import BaseCommand
from django.conf import settings

from account.models import *

class Command(BaseCommand):
        
    """
    Command class to create default users for the account
    application.

    Attributes:
        help (str): The help message for the command.

    Methods:
        handle(*args, **kwargs): Executes the command.
    """
    
    
    help = 'Create a default admin user if it does not exist.'

    def handle(self, *args, **kwargs):

        """
        Create default users for the application.

        Args: None

        Returns: None
        """

        users_data = [
            {'username': 'user1', 'password': 'user1'},
            {'username': 'user2', 'password': 'user2'},
            {'username': 'user3', 'password': 'user3'}
        ]
        try:
            for user_data in users_data:
                if not User.exists(user_data['username']):
                    User.create(user_data['username'], user_data['password'])
            self.stdout.write(self.style.SUCCESS('Users for account successfully populated.'))
        except Exception as e:
            self.stdout.write(self.style.WARNING('An error occurred while populating users for account.', e))
