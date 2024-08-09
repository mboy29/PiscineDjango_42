
from django.shortcuts import redirect
from django.urls import reverse

class MiddlewareRedirectAuthenticatedUser:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        restricted_paths = [
            reverse('ex:login'),
            reverse('ex:register')
        ]
        if request.user.is_authenticated and request.path in restricted_paths:
            return redirect('ex:home')
        response = self.get_response(request)
        return response
