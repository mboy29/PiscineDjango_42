from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):

    """
    Custom user admin class to manage users.

    Attributes:
        list_display (tuple): The list display fields.
        search_fields (tuple): The search fields.
        readonly_fields (tuple): The readonly fields.
    
    Methods:
        save_model(request, obj, form, change): Saves the model data.
    """

    list_display = ('username', 'email', 'is_staff', 'is_active', 'is_tip_admin_remover', 'is_tip_admin_downvoter')
    search_fields = ('username', 'email')
    readonly_fields = ('created_at',)
    
    def save_model(self, request, obj, form, change):

        """
        Saves the model data.

        Args:
            request (obj): The request object.
            obj (obj): The model object.
            form (obj): The form object.
            change (bool): The change flag.
        
        Returns: None
        """

        if not change:
            obj.set_password(obj.password)
        super().save_model(request, obj, form, change)

@admin.register(Tip)
class TipAdmin(admin.ModelAdmin):
    
    """
    Tip admin class to manage tips.

    Attributes:
        list_display (tuple): The list display fields.
        search_fields (tuple): The search fields.
    
    Methods:
        save_model(request, obj, form, change): Saves the model data.
    """

    list_display = ('author', 'upvotes', 'downvotes', 'date')
    search_fields = ('author', 'content')
