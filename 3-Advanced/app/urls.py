"""d05 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import *

app_name = 'app'

urlpatterns = [
    path('', ViewHome.as_view(), name='home'),
    path('home/', ViewHome.as_view(), name='home'),

    path('register/', ViewRegister.as_view(), name='register'),
    path('login/', ViewLogin.as_view(), name='login'),
    path('login/nav/', ViewLoginNav.as_view(), name='login_nav'),
    path('logout/', ViewLogout.as_view(), name='logout'),

    path('articles/', ViewArticles.as_view(), name='articles'),
    path('publications/', ViewPublications.as_view(), name='publications'),
    path('favourites/', ViewFavourites.as_view(), name='favourites'),
    path('favourites/<int:pk>/add/', AddToFavouritesView.as_view(), name='favourites_add'),
    path('details/<int:pk>/', ViewDetails.as_view(), name='details'),
    path('publish/', ViewPublish.as_view(), name='publish'),

    path('translate/', ViewTranslate.as_view(), name='translate'),
]

