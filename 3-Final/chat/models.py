from django.db import models

# Create your models here.

class ChatRoom(models.Model):

    """
    A class to represent a chat room.
    
    Attributes:
        name: The name of the room.
    
    Methods:
        __str__: Returns the name of the room.
        create: Creates a new room.
        exists: Checks if a room exists.
        fetch: Fetches a room.
        fetchall: Fetches all rooms.
    """
    
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):

        """
        String representation of the room.

        Args: None

        Returns: The name of the room.
        """

        return self.name
    
    @classmethod
    def create(cls, name):

        """
        Creates a new room.

        Args:
            name (str): The name of the room.
        
        Returns: The new room.
        """

        if not cls.exists(name):
            return cls.objects.create(name=name)
        return cls.fetch(name)
    
    @classmethod
    def exists(cls, name):

        """
        Checks if a room exists.

        Args:
            name (str): The name of the room.
        
        Returns: True if the room exists, False otherwise.
        """

        return cls.objects.filter(name=name).exists()

    @classmethod
    def fetch(cls, name):

        """
        Fetches a room.

        Args:
            name (str): The name of the room.
        
        Returns: The room.
        """

        return cls.objects.get(name=name)

    @classmethod
    def fetchall(cls):

        """
        Fetches all rooms.

        Args: None

        Returns: All rooms.
        """

        return cls.objects.all()