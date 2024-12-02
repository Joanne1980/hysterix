from django.urls import path
from .views import bio

urlpatterns = [
    path("", bio.as_view(), name ='bio'),
]