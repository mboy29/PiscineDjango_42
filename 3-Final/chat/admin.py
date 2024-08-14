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

@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    
    """
    Admin class for the Message model.
    
    Attributes:
        list_display (tuple): The fields to display in the list view.
        list_filter (tuple): The fields to filter by.
        search_fields (tuple): The fields to search by.
    
    Methods: None
    """
    
    list_display = ("room", "user", "message", "timestamp")
    list_filter = ("room", "user", "timestamp")
    search_fields = ("room", "user")
