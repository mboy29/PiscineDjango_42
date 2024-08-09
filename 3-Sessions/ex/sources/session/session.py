from django.http import JsonResponse

from .manager import *

def session_update(request) -> JsonResponse:
    
    """
    AJAX endpoint to update the anonymous username in the session.

    Args:
        request (HttpRequest): The request object.
    
    Returns:
        JsonResponse: The JSON response object
    """
    
    try:
        with SessionManager(request) as session_manager:
            remaining_time = session_manager.username_set()
            username = session_manager.username_fetch()
        return JsonResponse({'username': username, 'remaining_time': remaining_time})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def session_info(request) -> JsonResponse:

    """
    Returns a JSON response with the session information for the user
    (username and user ID).

    Args:
        request (HttpRequest): The request object.
    
    Returns:
        JsonResponse: The JSON response object.
    """
    try:
        with SessionManager(request) as session_manager:
            user = session_manager.user_fetch()
            username = session_manager.username_fetch()
        return JsonResponse({'user': user, 'username': username, })
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)