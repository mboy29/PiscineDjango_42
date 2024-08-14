from django.db import models

from account.models import *

class ChatRoom(models.Model):

    """
    Model class for the chat room.

    Attributes:
        name (str): The name of the chat room.
        users (ManyToManyField): The users in the chat room.
    
    Methods:
        fetch_messages: Fetches all messages in the chat room.
        fetch_users: Fetches all users in the chat room.
        users_add: Adds a user to the chat room.
        users_remove: Removes a user from the chat room.
        create: Creates a new chat room.
        exists: Checks if a chat room exists.
        fetch: Fetches a chat room by name.
        fetchall: Fetches all chat
    """

    name = models.CharField(max_length=255, unique=True)
    users = models.ManyToManyField(User, related_name='rooms')

    def __str__(self):

        """
        Returns the name of the chat room.

        Args:
            self (ChatRoom): The ChatRoom instance.
        
        Returns:
            str: The name of the chat room.
        """

        return self.name
    
    def fetch_messages(self):

        """
        Fetches all messages in the chat room.

        Args:
            self (ChatRoom): The ChatRoom instance.
        
        Returns:
            QuerySet: The messages in the chat room.
        """

        from .message import ChatMessage
        return ChatMessage.objects.filter(room=self).order_by('-timestamp')
    
    def fetch_users(self):

        """
        Fetches all users in the chat room.

        Args:
            self (ChatRoom): The ChatRoom instance.

        Returns:
            QuerySet: The users in the chat room.
        """

        return self.users.all()
    
    def users_add(self, user):

        """
        Adds a user to the chat room.

        Args:
            self (ChatRoom): The ChatRoom instance.
            user (User): The user to add.
        
        Returns: None
        """

        self.users.add(user)

    def users_remove(self, user):

        """
        Removes a user from the chat room.

        Args:
            self (ChatRoom): The ChatRoom instance.
            user (User): The user to remove.

        Returns: None
        """

        self.users.remove(user)

    @classmethod
    def create(cls, name):

        """

        Creates a new chat room.

        Args:
            cls (ChatRoom): The ChatRoom class.
            name (str): The name of the chat room.
        
        Returns:
            ChatRoom: The new chat room.
        """

        if not cls.exists(name):
            return cls.objects.create(name=name)
        return cls.fetch(name)
    
    @classmethod
    def exists(cls, name):

        """
        Checks if a chat room exists.

        Args:
            cls (ChatRoom): The ChatRoom class.
            name (str): The name of the chat room.
        
        Returns:
            bool: True if the chat room exists, False otherwise.
        """

        return cls.objects.filter(name=name).exists()
    
    @classmethod
    def fetch(cls, name):

        """
        Fetches a chat room by name.

        Args:
            cls (ChatRoom): The ChatRoom class.
            name (str): The name of the chat room.
        
        Returns:
            ChatRoom: The chat room with the given name.
        """
        return cls.objects.get(name=name)
    
    @classmethod
    def fetchall(cls):
        return cls.objects.all()
    
