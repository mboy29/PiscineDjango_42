from django.core.management.base import BaseCommand
from django.conf import settings
from app.models import User

class Command(BaseCommand):
        
    """
    Command class to create a default admin user if it does not exist.

    Attributes:
        help (str): The help message for the command.

    Methods:
        handle(*args, **kwargs): Executes the command.
    """
    
    
    help = 'Create a default admin user if it does not exist.'

    def handle(self, *args, **kwargs):

        """
        Executes the command.

        Args:
            *args: The arguments.
            **kwargs: The keyword arguments.
        
        Returns: None
        """

        admin_username = settings.ADMIN_USERNAME
        admin_password = settings.ADMIN_PASSWORD
        admin_email = settings.ADMIN_EMAIL

        if not User.objects.filter(username=admin_username).exists():
            User.objects.create_superuser(
                username=admin_username,
                password=admin_password,
                email=admin_email
            )
            self.stdout.write(self.style.SUCCESS('Admin user created successfully.'))
        else:
            self.stdout.write(self.style.WARNING('Admin user already exists.'))
