from rest_framework import serializers
from .models import modi

class sermodi(serializers.ModelSerializer):
    class Meta:
        model =modi
        fields= ['id','name','roll','city']
    