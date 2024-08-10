from django.db import models
from django.utils.translation import gettext_lazy as _

from .user import *

# Create your models here.

class Article(models.Model):

    """
    Custom article model class to create and manage articles.

    Attributes:
        title (str): The article title.
        author (obj): The article author.
        created (datetime): The article creation date.
        synopsis (str): The article synopsis.
        content (str): The article content.
    
    Methods:
        __str__(): Return the string representation of the article.
        create(data): Create a new article.
        exists(title): Check if an article exists.
        fetch(title): Get the article object.
        fetchall(): Fetch all articles.
    """

    title = models.CharField(max_length=64, null=False, blank=False, unique=True, verbose_name=_('Title'))
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, verbose_name=_('Author'))
    created = models.DateTimeField(auto_now_add=True, null=False, blank=False, verbose_name=_('Created'))
    synopsis = models.CharField(max_length=312, null=False, blank=False, verbose_name=_('Synopsis'))
    content = models.TextField(null=False, blank=False, verbose_name=_('Content'))

    class Meta:
        db_table = 'quickreads_article'
        verbose_name_plural = _("Articles")
    
    def __str__(self):
    
        """
        Return the string representation of the article.

        Args: None

        Returns:
            str: The title
        """

        return self.title  
    
    @classmethod
    def create(cls, data):
        """
        Create a new article.

        Args:
            data (dict): A dictionary containing article details (title, author, synopsis, content).
        
        Returns:
            Article: The new article object.
        
        Raises:
            ValueError: If 'author' in the data does not exist in the User model.
        """
        # Ensure the 'author' field in data corresponds to an existing User
        author = data.get('author')
        if not User.exists(author.username):
            raise ValueError(_('The specified author does not exist'))
        
        return cls.objects.create(**data)
    
    @classmethod
    def exists(cls, title):
        """
        Check if an article exists.

        Args:
            title (str): The article title.
        
        Returns:
            bool: True if the article exists, False otherwise.
        """

        return cls.objects.filter(title=title).exists()

    @classmethod
    def fetch(cls, **kwargs):
        """
        Fetch articles based on the provided keyword arguments.

        Args:
            **kwargs: Keyword arguments for filtering articles. Valid keys include 'title' and 'user'.

        Returns:
            QuerySet or Article: 
                - If both 'title' and 'user' are provided, returns a single article.
                - If only 'title' is provided, returns a single article.
                - If only 'user' is provided, returns a queryset of articles.
                - Returns an empty QuerySet or None if no matching articles are found.
        """
        title = kwargs.get('title')
        user = kwargs.get('user')

        if title and user:
            try:
                return cls.objects.get(title=title, author=user)
            except cls.DoesNotExist:
                return None
        elif title:
            try:
                return cls.objects.get(title=title)
            except cls.DoesNotExist:
                return None
        elif user:
            return cls.objects.filter(author=user).order_by('-created')
        return cls.objects.none()

    @classmethod
    def fetchall(cls, user):
        """
        Fetch all articles.

        Args: None

        Returns:
            list: The list of articles
        """

        return cls.objects.filter(author=user).order_by('-created')

    @classmethod
    def fetchall(cls):
    
        """
        Fetch all articles.

        Args: None

        Returns:
            list: The list of articles
        """

        return cls.objects.all().order_by('-created')
