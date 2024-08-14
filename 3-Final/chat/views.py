from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from chat.models.room import *

# Create your views here.

@login_required
def view_index(request) -> HttpResponse:

    """
    Renders the chat index page.

    Args:
        request: The request object.
    
    Returns:
        http.HttpResponse: The response object.

    """

    rooms = ChatRoom.fetchall()
    return render(request, "index.html", {"rooms": rooms})

@login_required
def view_room(request, room_name):

    """
    Renders the chat room page.

    Args:
        request: The request object.
        room_name: The name of the room.
    
    Returns:
        http.HttpResponse: The response object.
    """

    try:
        room = ChatRoom.fetch(room_name)
    except ChatRoom.DoesNotExist:
        messages.error(request, "The chat room does not exist.")
        return redirect('chat:index')
    return render(request, "room.html", {"room_name": room.name})