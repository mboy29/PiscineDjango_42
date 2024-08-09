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
from django.contrib import admin
from django.urls import path

from .views import *

app_name = 'ex'

urlpatterns = [
    path('', view_home, name='home'),
    path('register/', view_register, name='register'),
    path('login/', view_login, name='login'),
    path('logout/', view_logout, name='logout'),

    path('session/update/', session_update, name='session_update'),
    path('session/info/', session_info, name='session_info')
]
