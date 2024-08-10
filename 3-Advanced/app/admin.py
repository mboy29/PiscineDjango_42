from django.contrib import admin

from .models import *

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    """
    Custom user admin class to manage users.

    Attributes:
        list_display (tuple): The list display fields.
        search_fields (tuple): The search fields.
        readonly_fields (tuple): The readonly fields.
    
    Methods:
        save_model(request, obj, form, change): Saves the model data.
    """

    list_display = ('username', 'email', 'is_staff', 'is_active')
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

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    """
    Custom article admin class to manage articles.

    Attributes:
        list_display (tuple): The list display fields.
        search_fields (tuple): The search fields.
        readonly_fields (tuple): The readonly fields.
    
    Methods:
        save_model(request, obj, form, change): Saves the model data.
    """

    list_display = ('title', 'author', 'created')
    search_fields = ('title', 'author')
    readonly_fields = ('created',)

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

        super().save_model(request, obj, form, change)

@admin.register(UserFavouriteArticle)
class UserFavouriteArticleAdmin(admin.ModelAdmin):

    """
    Custom user favourite article admin class to manage user favourite articles.

    Attributes:
        list_display (tuple): The list display fields.
        search_fields (tuple): The search fields.
    
    Methods:
        save_model(request, obj, form, change): Saves the model data.
    """

    list_display = ('user', 'article')
    search_fields = ('user', 'article')

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

        super().save_model(request, obj, form, change)