import random
from datetime import datetime
from django.conf import settings
from django.utils import timezone
from django.http import JsonResponse

class SessionManager:
    
    """
    Session manager to handle a user's session.

    Attributes:
        request (HttpRequest): The request object.
        user (CustomUser): The user object.

    Methods:
        __init__(request): Initializes the session manager with the request object.
        __enter__(): Initializes the context manager and returns the instance.
        __exit__(exc_type, exc_value, traceback): Cleans up any resources or handles
            exceptions when exiting the context.
        username_clear(): Clears the username from the session.
        username_set(): Sets the username in the session if it doesn't exist or has
            expired.
        username_fetch(): Retrieves the username from the session.
    """

    def __init__(self, request):
        
        """
        Initializes the session manager with the request object.

        Args:
            request (HttpRequest): The request object.
        
        Returns: None
        """
        
        self.request = request

    def __enter__(self):
        
        """
        Initializes the context manager and returns the instance.

        Args: None 

        Returns: SessionManager instance
        """
        
        self.username_set()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        
        """
        Cleans up any resources or handles exceptions when exiting the context.

        Args:
            exc_type: The exception type.
            exc_value: The exception value.
            traceback: The traceback object.
        
        Returns: False
        """
        
        try:
            if exc_type is not None:
                raise Exception(f"[ERROR] {exc_value}")
            return False 
        except Exception as e:
            raise Exception(f"[ERROR] Could not exit session manager: {e}")
    

    def user_set(self, user):

        """
        Sets the user ID in the session and sets the username in 
        the session to the user's username.

        Args:
            user (CustomUser): The user object to set in the session.
        
        Returns: None
        """

        self.request.session['user'] = user.id
        self.username_set(user.username)
    
    def user_clear(self):

        """
        Clears the user ID from the session and clears the username from the 
        session.

        Args: None

        Returns: None
        """

        self.request.session.pop('user', None)
        self.username_clear()
        self.username_set()

    def user_fetch(self):

        """
        Retrieves the user ID from the session.

        Returns:
            int: The user ID from the session or None if it doesn't exist.
        """

        user = self.request.session.get('user')
        if not user:
            return None
        return user

    def username_set(self, username=None):
        
        """
        Sets the username in the session. If the username is not provided,
        it generates a random username from the settings.RANDOM_USERNAMES list
        every 42 seconds. The username is stored in the session along with the
        time it was created.

        Args:
            username (int): The username to set in the session. Defaults to None.

        Returns:
            `remaining_time` is the seconds left before the username expires.
            
        Raises:
            Exception: If there was an error setting the username in the session.
        """
        
        try:
            if username:
                self.username_clear()
                self.request.session['username'] = username
                return -1
            elif self.user_fetch():
                return -1
            username = self.request.session.get('username')
            username_created_at = self.request.session.get('username_created_at')
            if not username or (timezone.now() - datetime.fromisoformat(username_created_at)).seconds >= 42:
                self.username_clear()
                username = random.choice(settings.RANDOM_USERNAMES)
                username_created_at = timezone.now().isoformat()
                self.request.session['username'] = username
                self.request.session['username_created_at'] = username_created_at
            created_at = datetime.fromisoformat(username_created_at)
            elapsed_time = (timezone.now() - created_at).seconds
            remaining_time = max(0, 42 - elapsed_time)
            return remaining_time
        except Exception as e:
            raise Exception(f"[ERROR] Could not set username in session: {e}")

    def username_clear(self):
        
        """
        Clears the username and the username_created_at from the session.

        Args: None

        Returns: None

        Raises:
            Exception: If there was an error clearing the username from the session.
        """
        
        try:
            self.request.session.pop('username', None)
            self.request.session.pop('username_created_at', None)
        except Exception as e:
            raise Exception(f"[ERROR] Could not clear username from session: {e}")

    def username_fetch(self):
        
        """
        Retrieves the username from the session.

        Returns:
            str: The username from the session.
        
        Raises:
            Exception: If there was an error retrieving the username from the session.
        """
        
        try:
            return self.request.session.get('username', 'default')
        except Exception as e:
            raise Exception(f"[ERROR] Could not get username from session: {e}")