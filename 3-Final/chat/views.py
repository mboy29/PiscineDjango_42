from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from chat.models import *

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

    room = ChatRoom.create(room_name)
    return render(request, "room.html", {"room_name": room.name})