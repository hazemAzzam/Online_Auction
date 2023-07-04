from rest_framework.serializers import ModelSerializer, CharField
from .models import *

class Category_Serializer(ModelSerializer):
    
    class Meta:
        model=Category
        fields="__all__"
        