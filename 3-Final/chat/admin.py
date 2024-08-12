from django.contrib import admin

from chat.models import *

# Register your models here.

@admin.register(ChatRoom)
class ChatRoomAdmin(admin.ModelAdmin):
    
    """
    Admin class for the Room model.
    
    Attributes:
        list_display (tuple): The fields to display in the list view.
    
    Methods: None
    """
    
    list_display = ("name",)