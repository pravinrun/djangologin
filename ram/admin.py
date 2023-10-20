from django.contrib import admin
from .models import indore

@admin.register(indore)
class indore(admin.ModelAdmin):
    list_display=['name','gmail','passw','mobile','date']

# Register your models here.
