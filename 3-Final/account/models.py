from django.db import models
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.

class UserManager(BaseUserManager):

    """
    User manager class to create and manage users.

    Attributes:
        _db (str): The database name.
        
    Methods:
        create_user(username, password, **extra_fields): Create a new user.
        create_superuser(username, password, **extra_fields): Create a new superuser.
    """

    def create_user(self, username, password=None, **extra_fields):

        """
        Create and return a new user with an email and password.

        Args:
            username (str): The username.
            password (str): The password.
            **extra_fields: The extra fields.
        
        Returns:
            User: The new user object.
        """

        if not username:
            raise ValueError('The Username field must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
            
        """
        Create and return a new superuser with an email and password.

        Args:
            username (str): The username.
            password (str): The password.
            **extra_fields: The extra fields.
        
        Returns:
            User: The new superuser object.
        """

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):

    """
    Custom user model class to create and manage users.

    Attributes:
        username (str): The username.
        email (str): The email.
        password (str): The password.
        created_at (DateTimeField): The created date and time.
        is_active (bool): The active status.
        is_staff (bool): The staff status.
    
    Methods:
        __str__(): Return the string representation of the user.
        create(username, password, **extra_fields): Create and return a new user.
        exists(username): Check if the user exists.
        fetch(username): Get the user object.
        fetchall(): Get all the user objects.
    """
    
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(blank=True, null=True)
    password = models.CharField(max_length=128)
    created_at = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    
    class Meta:
        db_table = 'ex_User'
        verbose_name_plural = "Custom Users"
    
    def __str__(self):

        """
        Return the string representation of the user.

        Args: None

        Returns:
            str: The username
        """

        return self.username
    
    @classmethod
    def create(cls, username, password, **extra_fields):
        
        """
        Class method to create and return a new user with hashed password.
        
        Args:
            username (str): The username.
            password (str): The password.
            **extra_fields: The extra fields.

        Returns:
            User: The new user object.
        """
       
        if not username:
            raise ValueError('The Username field must be set')
        user = cls(username=username, **extra_fields)
        user.set_password(password)  # Hash the password
        user.save()
        return user
    
    @classmethod
    def exists(cls, username):

        """
        Class method to check if the user exists.

        Args:
            username (str): The username.
        
        Returns:
            bool: True if the user exists, False otherwise.
        """

        return cls.objects.filter(username=username).exists()

    @classmethod
    def fetch(cls, username):
            
        """
        Class method to get the user object.

        Args:
            username (str): The username.

        Returns:
            User: The user object.
        """

        return cls.objects.get(username=username)
    
    @classmethod 
    def fetchall(cls):

        """
        Class method to get all the user objects.

        Args: None

        Returns:
            QuerySet: The user objects
        """

        return cls.objects.all()
