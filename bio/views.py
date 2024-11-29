from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from .models import bio

# Create your views here.

#def bio (generic.BioView):
def bio(request):
    return HttpResponse("Hello, Django!")

  #queryset = bio.objects.all()
  #template_name = "bio.html"