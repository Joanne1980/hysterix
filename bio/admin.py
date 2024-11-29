from django.contrib import admin
from .models import bio
from django_summernote.admin import SummernoteModelAdmin


@admin.register(bio)
#class BioAdmin(SummernoteModelAdmin):

class bioAdmin(SummernoteModelAdmin): 
    summernote_fields = '__all__'

# Register your models here.

