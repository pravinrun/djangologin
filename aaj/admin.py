from django.contrib import admin
from . models import modi

# Register your models here.
@admin.register(modi)
class ModiAdmin(admin.ModelAdmin):
    list_display=['name','roll','city']
    


    


