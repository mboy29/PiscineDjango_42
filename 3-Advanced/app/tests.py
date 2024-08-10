from django.test import TestCase, Client
from django.urls import reverse
from app.models import *

class AuthenticatedViewsTests(TestCase):

    """
    Test that authenticated views are only accessible by registered users.

    Attributes: None

    Methods:
        setUp: Create a test user and log the user in.
        test_favourites_view_requires_login: Test that the favourites 
            view is only accessible by registered users.
        test_publications_view_requires_login: Test that the publications
            view is only accessible by registered users.
        test_publish_view_requires_login: Test that the publish view
            is only accessible by registered users.
    """

    def setUp(self):

        """
        Create a test user and log the user in.

        Args: None

        Returns: None
        """

        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client = Client()

    def test_favourites_view_requires_login(self):
        
        """
        Test that the favourites view is only accessible by registered users.
        
        Args: None
        
        Returns: None
        """
        
        response = self.client.get(reverse('app:favourites'), follow=True)
        self.assertRedirects(response, reverse('app:articles'))

    def test_publications_view_requires_login(self):
        
        """
        Test that the publications view is only accessible by registered users.
        
        Args: None
        
        Returns: None
        """

        response = self.client.get(reverse('app:publications'), follow=True)
        self.assertRedirects(response, reverse('app:articles'))

    def test_publish_view_requires_login(self):
        
        """
        Test that the publish view is only accessible by registered users.
        
        Args: None
        
        Returns: None
        """

        response = self.client.get(reverse('app:publish'), follow=True)
        self.assertRedirects(response, reverse('app:articles'))


class RegistrationAccessTests(TestCase):

    """
    Test that a registered user cannot access the registration form.

    Attributes: None

    Methods:
        setUp: Create a test user and log the user in.
        test_registered_user_cannot_access_registration: Test that a registered user cannot access the registration form.
    """

    def setUp(self):
        
        """
        Create a test user and log the user in.

        Args: None

        Returns: None
        """
        
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client = Client()
        self.client.login(username='testuser', password='testpassword')

    def test_registered_user_cannot_access_registration(self):
        
        """
        Test that a registered user cannot access the registration form.
        
        Args: None

        Returns: None
        """

        response = self.client.get(reverse('app:register'), follow=True)
        self.assertRedirects(response, reverse('app:articles'))


class FavouriteTests(TestCase):

    """
    Test the favourite functionality (can't add the same article twice).

    Attributes: None

    Methods:
        setUp: Create a test user, article and log the user in.
        test_user_cannot_add_article_to_favourites_twice: Test that a user cannot add the same article to their favourites twice
    """

    def setUp(self):

        """
        Create a test user, article and log the user in.

        Args: None

        Returns: None
        """

        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.article = Article.objects.create(title='Test Article', synopsis='Test Synopsis', content='Test Content', author=self.user)
        self.client = Client()
        self.client.login(username='testuser', password='testpassword')

    def test_user_cannot_add_article_to_favourites_twice(self):
        
        """
        Test that a user cannot add the same article to their 
        favourites twice.

        Args: None
        
        Returns: None
        """
        self.client.post(reverse('app:favourites_add', args=[self.article.id]), follow=True)
        self.assertEqual(UserFavouriteArticle.objects.filter(user=self.user, article=self.article).count(), 1)

        response = self.client.post(reverse('app:favourites_add', args=[self.article.id]), follow=True)
        self.assertEqual(UserFavouriteArticle.objects.filter(user=self.user, article=self.article).count(), 1)
        self.assertContains(response, "already in favourites", status_code=200)

        self.assertEqual(UserFavouriteArticle.objects.count(), 1)
