from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class bio(models.Model):
    artist = models.CharField(max_length=200)
    image = models.ImageField()
    content = models.TextField()
    social_links = models.CharField()
    slug = models.SlugField
