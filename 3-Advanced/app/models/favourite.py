from django.db import models

from .user import *
from .article import *

# Create your models here.

class UserFavouriteArticle(models.Model):

    """
    Custom user favourite article model class to create and manage user favourite articles.

    Attributes:
        user (obj): The user.
        article (obj): The article.

    Methods:
        __str__(): Return the string representation of the user favourite article.
        create(data): Create a new user favourite article.
        exists(user, article): Check if a user favourite article exists.
        fetchall(): Fetch all articles.
        fetch(user): Fetch all articles from the given user.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=False, blank=False)

    class Meta:
        db_table = 'quickreads_user_favourite_article'
        verbose_name_plural = "User Favourite Articles"
    
    def __str__(self):
    
        """
        Return the string representation of the user favourite article.

        Args: None

        Returns:
            str: The user and article title
        """

        return self.article.title
    
    @classmethod
    def create(cls, user, article):
        
        """
        Create a new user favourite article.

        Args:
            user (User): The user.
            article (Article): The article.
        
        Returns:
            UserFavouriteArticle: The new user favourite article object.
        """
        
        return cls.objects.create(user=user, article=article)

    @classmethod
    def exists(cls, user, article):
    
        """
        Check if a user favourite article exists.

        Args:
            user (User): The user.
            article (Article): The article.

        Returns:
            bool: True if the user favourite article exists, False otherwise.
        """

        return cls.objects.filter(user=user, article=article).exists()

    @classmethod
    def fetchall(cls):
    
        """
        Fetch all articles.

        Args: None

        Returns:
            list: The list of articles
        """

        return cls.objects.all()

    @classmethod
    def fetch(cls, user):
    
        """
        Fetch all articles from the given user.

        Args:
            user (obj): The user.

        Returns:
            list: The list of articles
        """

        favourites = cls.objects.filter(user=user)
        if not favourites:
            return []
        return [favourite.article for favourite in favourites]