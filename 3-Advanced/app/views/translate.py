import re
from django.conf import settings
from django.http import HttpResponseRedirect
from django.utils.translation import activate
from django.views.generic.base import RedirectView

class ViewTranslate(RedirectView):

    """
    View to change the language of the website. 
    Redirects to the same page in the other language.
    Methods:
        get_redirect_url: Determine the URL to redirect to.
    """

    def get_redirect_url(self, *args, **kwargs):
        current_url = self.request.META.get('HTTP_REFERER').replace('http://127.0.0.1:8000', '')
        match = re.match(r'^/([a-z]{2})/', current_url)
        if match:
            current_language = match.group(1)
        else:
            current_language = settings.LANGUAGE_CODE[:2]
        languages = [lang[0] for lang in settings.LANGUAGES]
        other_languages = [lang for lang in languages if lang != current_language]
        if not other_languages:
            return current_url
        next_language = other_languages[0]
        new_url = re.sub(r'^/([a-z]{2})/', f'/{next_language}/', current_url, count=1)
        activate(next_language)
        return new_url
