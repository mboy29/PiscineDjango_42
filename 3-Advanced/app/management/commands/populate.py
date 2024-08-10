from django.utils.timezone import now
from django.core.management.base import BaseCommand

from app.models import *

class Command(BaseCommand):
    
    """
    Django management command to populate the database with 
    default users and articles.

    Methods:
        handle: Entry point of the command. Creates users and articles.
    """

    help = 'Create initial users and articles for the application.'

    def populate_users(self):

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
        users = []
        for user_data in users_data:
            if not User.exists(user_data['username']):
                user = User.create(**user_data)
            else:
                user = User.fetch(user_data['username'])
            users.append(user)
        return users

    def populate_articles(self, users):

        """
        Create initial articles from the previously created users.

        Args:
            users (list): A list of User objects.
        
        Returns: None
        """

        articles_data = [
            {'title': 'Article 1', 'author': users[0], 'synopsis': 'Synopsis of article 1 - other 20 characters to demonstrate what ex03 demands.', 'content': 'Content of article 1'},
            {'title': 'Article 2', 'author': users[0], 'synopsis': 'Synopsis article 2', 'content': 'Content article 2'},
            {'title': 'Article 3', 'author': users[1], 'synopsis': 'Synopsis article 3', 'content': 'Content article 3'},
            {'title': 'Article 4', 'author': users[1], 'synopsis': 'Synopsis article 4', 'content': 'Content article 4'},
            {'title': 'Article 5', 'author': users[2], 'synopsis': 'Synopsis article 5', 'content': 'Content article 5'}
        ]
        articles = []
        for article_data in articles_data:
            if not Article.exists(article_data['title']):
                article = Article.create(article_data)
            else:
                article = Article.fetch(title=article_data['title'])
            articles.append(article)
        
        return articles

    def populate_favourites(self, users, articles):

        """
        Create initial favourites for the application.

        Args:
            users (list): A list of User objects.
            articles (list): A list of Article objects.
        
        Returns: None
        """

        favourites_data = [
            {'user': users[0], 'article': articles[0]},
            {'user': users[0], 'article': articles[1]},
            {'user': users[1], 'article': articles[2]},
            {'user': users[1], 'article': articles[3]},
            {'user': users[2], 'article': articles[4]}
        ]
        for favourite_data in favourites_data:
            UserFavouriteArticle.create(user=favourite_data['user'], article=favourite_data['article'])

    def handle(self, *args, **options):
        
        """
        Populate the database with default users and articles.

        Args:
            *args: Variable length argument list.
            **options: Arbitrary keyword arguments.

        Returns:
            None
        """

        try:
            users = self.populate_users()
            articles = self.populate_articles(users)
            self.populate_favourites(users, articles)
            self.stdout.write(self.style.SUCCESS('Data population complete.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'An error occurred: {e}'))
       
