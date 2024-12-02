from django.views.generic import TemplateView


# Create your views here.

class bio(TemplateView):
    template_name = 'bio/bio.html'