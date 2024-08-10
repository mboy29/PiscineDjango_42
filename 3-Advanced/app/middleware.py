from django.urls import reverse
from django.shortcuts import redirect

class MiddlewareRedirectUser:

    """
    Middleware class to redirect users depending on 
    their authentication status and the path they are
    trying to access.

    Attributes:
        get_response (function): The next middleware function.

    Methods:
        __init__(get_response): The constructor
        __call__(request): The middleware function.
    """

    def __init__(self, get_response):

        """
        The constructor for the MiddlewareRedirectUser class.
        
        Args:
            get_response (function): The next middleware function.

        Returns: None
        """

        self.get_response = get_response

    def __call__(self, request):
        
        """ 
        The middleware function to redirect users depending on
        their authentication status and the path they are 
        trying to access.
        
        Args:
            request (HttpRequest): The request object.
        
        Returns:
            HttpResponse: The HTTP response object.
        """

        authenticated_restricted_paths = [
            reverse('app:register'),
            reverse('app:login'),
        ]
        unauthenticated_restricted_patterns = [
            reverse('app:publications'),
            reverse('app:favourites'),
            reverse('app:publish'),
            reverse('app:logout'),
            '/details/',
        ]
        if request.user.is_authenticated:
            if request.path in authenticated_restricted_paths:
                return redirect('app:home')
        if not request.user.is_authenticated:
            for pattern in unauthenticated_restricted_patterns:
                if request.path.startswith(pattern):
                    return redirect('app:home')
        response = self.get_response(request)
        return response

