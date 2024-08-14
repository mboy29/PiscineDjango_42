from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth import logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from chat.models import *

@csrf_exempt
def view_account(request):

    """
    Renders the account page.

    Args:
        request: The request object.
    
    Returns:
        http.HttpResponse: The response object.
    """

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors})
    else:
        form = AuthenticationForm()
    return render(request, 'account.html', {'form': form, 'rooms': ChatRoom.fetchall()})


@csrf_exempt
def view_logout(request):

    """
    Logs out the user.

    Args:
        request: The request object.
    
    Returns:
        http.JsonResponse: The response object.
    """
    
    if request.method == 'POST':
        logout(request)
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'})