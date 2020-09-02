from django.shortcuts import render

from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

# Herencias multiples
class Home(LoginRequiredMixin, generic.TemplateView):
    template_name = 'bases/home.html'
    login_url = 'bases:login'

class HomeSinPrivilegios(generic.TemplateView):
    template_name = 'bases/sin_privilegios.html'