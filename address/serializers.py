from rest_framework.customs import ComplexSerializer, ModelSerializer
from .models import *

class Address_Serializer(ComplexSerializer):
    class Meta:
        model=Address
        fields="__all__"