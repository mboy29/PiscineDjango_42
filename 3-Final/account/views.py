from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

# Create your views here.

@csrf_exempt
def view_account(request):

    """
    Logs in the user.

    Args:
        request: The request object.

    Returns:
        JsonResponse: The JSON response object.
    """
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return JsonResponse({'status': 'logged_in', 'username': user.username})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors.as_json()})
    else:
        if request.user.is_authenticated:
            return JsonResponse({'status': 'logged_in', 'username': request.user.username})
        else:
            return render(request, 'account.html')

@login_required
@csrf_exempt
def view_logout(request) -> JsonResponse:

    """
    Logs out the user.

    Args:
        request: The request object.
    
    Returns:
        JsonResponse: The JSON response object.
    """
    
    if request.method == 'POST':
        logout(request)
        return JsonResponse({'status': 'logged_out'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
