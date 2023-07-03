from rest_framework.serializers import ModelSerializer
from rest_framework.customs import ComplexSerializer
from .models import *
from address.serializers import Address_Serializer
from django.contrib.auth.hashers import make_password

class Member_Serializer(ComplexSerializer):
    home_address = Address_Serializer(required=False)
    class Meta:
        model=Member
        fields="__all__"
        extra_kwargs={
            'password': {
                'write_only': True,
            },
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        address = validated_data.pop('home_address', None)
        if not password:
            raise ValueError("Please fill required fields")
        
        if address:
            address_serializer = Address_Serializer(data=address)
            address_serializer.is_valid(raise_exception=True)
            address = address_serializer.save()
            validated_data['home_address'] = address

        validated_data['password'] = make_password(password)
        user = super().create(validated_data)

        return user
