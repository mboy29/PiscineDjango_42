
from django.shortcuts import redirect
from django.urls import reverse

class MiddlewareRedirectAuthenticatedUser:

    """
    Middleware class to redirect authenticated users to 
    the home page.

    Attributes:
        get_response (function): The next middleware function.

    Methods:
        __init__(get_response): The constructor
        __call__(request): The middleware function.
    """

    def __init__(self, get_response):

        """
        The constructor for the MiddlewareRedirectAuthenticatedUser class.
        
        Args:
            get_response (function): The next middleware function.

        Returns:
            None
        """

        self.get_response = get_response

    def __call__(self, request):

        """ 
        The middleware function to redirect authenticated users to 
            the home page.
        
        Args:
            request (HttpRequest): The request object.
        
        Returns:
            HttpResponse: The HTTP response object.
        """

        restricted_paths = [
            reverse('ex:login'),
            reverse('ex:register')
        ]
        if request.user.is_authenticated and request.path in restricted_paths:
            return redirect('ex:home')
        response = self.get_response(request)
        return response
