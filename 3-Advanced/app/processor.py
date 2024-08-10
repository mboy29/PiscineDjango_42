from app.forms import FormLogin

def login_form_processor(request):
    """
    Context processor to include the login form in all templates.
    """
    return {
        'login_form': FormLogin()
    }