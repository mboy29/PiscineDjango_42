from django.db import models
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.

class CustomUserManager(BaseUserManager):

    """
    Custom user manager class to create and manage users.

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
            CustomUser: The new user object.
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
            CustomUser: The new superuser object.
        """

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):

    """
    Custom user model class to create and manage users.

    Attributes:
        username (str): The username.
        email (str): The email.
        password (str): The password.
        created_at (DateTimeField): The created date and time.
        is_active (bool): The active status.
        is_staff (bool): The staff status.
        objects (CustomUserManager): The custom user manager object.
        is_tip_admin_remover (bool): The tip admin remover status.
        is_tip_admin_downvoter (bool): The tip admin downvoter status.
        reputation (int): The reputation of the user.
    
    Methods:
        __str__(): Return the string representation of the user.
        user_create(username, password, **extra_fields): Create and return a new user.
        exists(username): Check if the user exists.
        fetch(username): Get the user object.
    """
    
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(blank=True, null=True)
    password = models.CharField(max_length=128)
    created_at = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    reputation = models.IntegerField(default=0)
    is_tip_admin_remover = models.BooleanField(default=False)
    is_tip_admin_downvoter = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    
    class Meta:
        db_table = 'ex_customuser'
        verbose_name_plural = "Custom Users"
    
    def __str__(self):

        """
        Return the string representation of the user.

        Args: None

        Returns:
            str: The username
        """

        return self.username
    
    def reputation_update(self, amount):
            
        """
        Update the user's reputation.

        Args:
            amount (int): The amount to update the reputation by.

        Returns: None
        """

        self.reputation += amount
        if self.reputation >= 15 and self.is_tip_admin_downvoter == False:
            self.is_tip_admin_downvoter = True
        if self.reputation < 15 and self.is_tip_admin_downvoter == True:
            self.is_tip_admin_downvoter = False
        if self.reputation >= 30 and self.is_tip_admin_remover == False:
            self.is_tip_admin_remover = True
        if self.reputation < 30 and self.is_tip_admin_remover == True:
            self.is_tip_admin_remover = False
        self.save()

    @classmethod
    def create(cls, username, password=None, **extra_fields):
        
        """
        Class method to create and return a new user with hashed password.
        
        Args:
            username (str): The username.
            password (str): The password.
            **extra_fields: The extra fields.

        Returns:
            CustomUser: The new user object.
        """
       
        if not username:
            raise ValueError('The Username field must be set')
        user = cls(username=username, **extra_fields)
        user.set_password(password)  # Hash the password
        user.save(using=cls._state.db)
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
            CustomUser: The user object.
        """

        return cls.objects.get(username=username)


class Tip(models.Model):

    """
    Tip model class to create and manage tips.

    Attributes:
        content (str): The content of the tip.
        author (CustomUser): The author of the tip.
        date (DateTimeField): The date and time of the tip.
        upvotes (int): The upvotes count.
        downvotes (int): The downvotes count.
        upvoters (ManyToManyField): The upvoters.
        downvoters (ManyToManyField): The downvoters.
    
    Methods:
        __str__(): Return the string representation of the tip.
        upvote(user): Upvote the tip.
        downvote(user): Downvote the tip.
        remove(): Remove the tip.
        create(content, author): Create a new tip.
        fetch(tip_id): Retrieve a tip by its ID.
        fetchall(): Retrieve all tips.
    """

    content = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    upvoters = models.ManyToManyField(CustomUser, related_name='upvoters')
    downvoters = models.ManyToManyField(CustomUser, related_name='downvoters')

    class Meta:
        
        """
        Meta class for the Tip model. 

        Attributes:
            ordering (list): The ordering of the tips.
        """

        ordering = ['-date']
    

    def __str__(self):

        """
        Return the string representation of the tip.

        Args: None

        Returns:
            str: The tip string.
        """

        return f'Tip by {self.author} on {self.date}'


    def upvote(self, user):

        """
        Handle the upvoting of the tip. If the user has already downvoted 
        the tip, the downvote is removed and the upvote is added. 
        If the user has already upvoted the tip, the upvote is removed.
        Otherwise, the upvote is added.

        Args:
            user (CustomUser): The user object.
        
        Returns: None

        Raises:
            Exception: If an error occurs.
        """

        try:
            if user in self.downvoters.all() and not user.is_tip_admin_downvoter:
                raise Exception('You\'re downvote privileges have been revoked, you can nologer downvote to upvote this tip.')
            if user == self.author:
                raise Exception('You cannot upvote your own tip.')
            elif user in self.downvoters.all():
                self.downvote(user)
                self.upvotes += 1
                self.upvoters.add(user)
                self.author.reputation_update(5)
            elif user in self.upvoters.all():
                self.upvotes -= 1 if self.upvotes > 0 else 0
                self.upvoters.remove(user)
                self.author.reputation_update(-5)
            else:
                self.upvotes += 1
                self.upvoters.add(user)
                self.author.reputation_update(5)
            self.save()
        except Exception as e:
            raise Exception(e)
    
    def downvote(self, user):

        """
        Handle the downvoting of the tip. If the user has already upvoted
        the tip, the upvote is removed and the downvote is added.
        If the user has already downvoted the tip, the downvote is removed.
        Otherwise, the downvote is added.

        Args:
            user (CustomUser): The user object.

        Returns: None

        Raises:
            Exception: If an error occurs.
        """

        try:
            if user == self.author:
                raise Exception('You cannot downvote your own tip.')
            elif not user.is_tip_admin_downvoter:
                raise Exception('You are not authorized to downvote this tip.')
            elif user in self.upvoters.all():
                self.upvote(user)
                self.downvotes += 1
                self.downvoters.add(user)
                self.author.reputation_update(-2)
            elif user in self.downvoters.all():
                self.downvotes -= 1 if self.downvotes > 0 else 0
                self.downvoters.remove(user)
                self.author.reputation_update(2)
            else:
                self.downvotes += 1
                self.downvoters.add(user)
                self.author.reputation_update(-2)
            self.save()
        except Exception as e:
            raise Exception(e)
    
    def remove(self, user):

        """
        Remove the tip.

        Args: None

        Returns: None

        Raises:
            Exception: If an error occurs.
        """

        try:
            if user != self.author and not user.is_tip_admin_remover:
                raise Exception('You are not authorized to delete this tip.')
            self.author.reputation_update(-(self.upvotes * 5) + (self.downvotes * 2))
            self.delete()
        except Exception as e:
            raise Exception(e)


    @classmethod
    def create(cls, content, author):
        
        """
        Class method to create a new tip.

        Args:
            content (str): The content of the tip.
            author (CustomUser): The user who is creating the tip.

        Returns:
            Tip: The created Tip instance.
        """
        
        return cls.objects.create(content=content, author=author)

    @classmethod
    def fetch(cls, tip_id):
        
        """
        Class method to retrieve a tip by its ID.

        Args:
            tip_id (int): The ID of the tip to retrieve.

        Returns:
            Tip: The Tip instance, or None if not found.
        """
        
        try:
            return cls.objects.get(id=tip_id)
        except cls.DoesNotExist:
            return None
    
    @classmethod
    def fetchall(cls):
        
        """
        Class method to retrieve all tips.

        Args: None

        Returns:
            QuerySet: The queryset of all tips.
        """
        
        return cls.objects.all()
