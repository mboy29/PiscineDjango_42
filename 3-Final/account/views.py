from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

def view_index(request):

    """
    View for the account index page.

    Params:
        request: The request object.

    Returns:
        The response object.
    """

    if request.is_ajax() and request.method == 'GET':
        return JsonResponse({
            'success': True,
            'user_is_authenticated': request.user.is_authenticated,
            'username': request.user.username
        })
    return render(request, 'account.html')

@csrf_exempt
def login_view(request):
    
    """
    View for the login page.

    Params:
        request: The request object.

    Returns:
        The response object.
    """

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'error': form.errors.as_json()})
    return JsonResponse({'success': False, 'error': 'Invalid request'})

@csrf_exempt
@login_required
def logout_view(request):

    """
    View for the logout page.

    Params:
        request: The request object.
    
    Returns:
        The response object.
    """

    if request.method == 'POST':
        logout(request)
        return JsonResponse({'success': True})
    return JsonResponse({'success': False, 'error': 'Invalid request'})
