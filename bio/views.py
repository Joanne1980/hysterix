from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePage(TemplateView):
    """
    displays home HomePage
    """
    template_name = 'index.html'
