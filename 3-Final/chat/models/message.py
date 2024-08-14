from django.db import models
from .room import ChatRoom
from account.models import User

class ChatMessage(models.Model):

    """
    Model class for the chat message.

    Attributes:
        room (ForeignKey): The chat room the message belongs to.
        user (ForeignKey): The user who sent the message.
        message (str): The message content.
        timestamp (DateTimeField): The timestamp of the message.
    
    Methods:
        create: Creates a new chat message.
        fetch: Fetches a chat message by room or user.
        fetchall: Fetches all chat messages.
    """

    room = models.ForeignKey(ChatRoom, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        """
        Returns the chat message as a string.

        Args:
            self (ChatMessage): The ChatMessage instance.
        
        Returns:
            str: The chat message.
        """

        return f'[{self.timestamp}] {self.user.username}: {self.message}'
    
    @classmethod
    def create(cls, room, user, message):

        """
        Creates a new chat message.

        Args:
            cls (ChatMessage): The ChatMessage class.
            room (ChatRoom): The chat room the message belongs to.
            user (User): The user who sent the message.
            message (str): The message content.
        
        Returns:
            ChatMessage: The new chat message.
        """

        return cls.objects.create(room=room, user=user, message=message)
    
    @classmethod
    def fetch(cls, **kwargs):

        """
        Fetches a chat message by room or user.

        Args:
            cls (ChatMessage): The ChatMessage class.
            **kwargs: The keyword arguments to filter by.  
        
        Returns:
            ChatMessage: The chat message.
        
        Raises:
            ValueError: If no valid keyword arguments are provided.
        """

        if 'room' not in kwargs and 'user' not in kwargs:
            raise ValueError('No valid keyword arguments provided.')
        return cls.objects.get(**kwargs)

    @classmethod
    def fetchall(cls):

        """
        Fetches all chat messages.

        Args:
            cls (ChatMessage): The ChatMessage class.

        Returns:
            QuerySet: All chat messages
        """
        
        return cls.objects.all().order_by('timestamp')
