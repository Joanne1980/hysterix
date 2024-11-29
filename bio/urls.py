from .import views
from django.urls import path

urlpatterns = [
    path("", bio.as_views(), name = 'bio'),
]