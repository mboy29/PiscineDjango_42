from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def view_index(request) -> HttpResponse:

    """
    Render a page with a table of colors and their shades.
    This includes shades of black, red, blue, and green.

    Args:
        request: HttpRequest object.
    Returns:
        HttpResponse object.
    """

    color_names = ["Black", "Red ", "Blue", "Green"]
    colors = []

    for i in range(50):
        val = f"{int(i * 255 / 50):02X}"
        black = "#" + val * 3 
        red = "#" + val + "0000"
        green = "#" + "00" + val + "00" 
        blue = "#" + "0000" + val
        colors.append((black, red, blue, green))
    
    return render(request, 'ex03/index.html', {
        'color_names': color_names, 
        'colors': colors
    })

