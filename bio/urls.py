from .import views
from django.urls import path

urlpatterns = [
    path("", views.Bio.as_view(), name='bio'),
]