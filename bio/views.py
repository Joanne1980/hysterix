from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class Bio(TemplateView):
    """
    displays home HomePage
    """
    template_name = 'bio.html'
