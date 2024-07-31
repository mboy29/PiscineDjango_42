from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.conf import settings

class Command(BaseCommand):
    help = 'Create a default admin user if it does not exist.'

    def handle(self, *args, **kwargs):
        admin_username = settings.ADMIN_USERNAME
        admin_password = settings.ADMIN_PASSWORD
        admin_email = settings.ADMIN_EMAIL

        if not User.objects.filter(username=admin_username).exists():
            User.objects.create_superuser(admin_username, admin_email, admin_password)
            self.stdout.write(self.style.SUCCESS('Admin user created successfully.'))
        else:
            self.stdout.write(self.style.WARNING('Admin user already exists.'))
