from django.core.management.base import BaseCommand
from django.conf import settings

from chat.models.room import *

class Command(BaseCommand):
        
    """
    Command class to create a rooms for chat.

    Attributes:
        help (str): The help message for the command.

    Methods:
        handle(*args, **kwargs): Executes the command.
    """
    
    
    help = 'Create a default admin user if it does not exist.'

    def handle(self, *args, **kwargs):

        """
        Create default chatrooms for the application.

        Args: None

        Returns: list of Chatroom objects
        """
        chatrooms_data = [
            'General',
            'Random',
            'Announcements',
        ]

        try:
            for name in chatrooms_data:
                if not ChatRoom.exists(name):
                    ChatRoom.create(name=name)
            self.stdout.write(self.style.SUCCESS('Rooms for chat successfully populated.'))
        except Exception as e:
            self.stdout.write(self.style.WARNING('An error occurred while populating rooms for chat.', e))
