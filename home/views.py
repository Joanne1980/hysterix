from django.views.generic import TemplateViews

# Create your views here.
class index(TemplateViews):
    template_name = 'home/index.html'