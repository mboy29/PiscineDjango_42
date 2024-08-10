from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from app.models import *
from app.forms import *

class ViewPublish(LoginRequiredMixin, CreateView):
    model = Article
    form_class = FormArticle
    template_name = 'publish.html'
    success_url = reverse_lazy('app:publications')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
