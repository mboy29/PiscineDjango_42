# IMPORTS
# -------
from django.urls import path
from . import views


# URL PATTERNS
# ------------

# Define the URL patterns for the helloworld app.

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
]