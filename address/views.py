from rest_framework.viewsets import ModelViewSet
from .serializers import *

# Create your views here.
class Address_View(ModelViewSet):
    queryset=Address.objects.all()
    serializer_class=Address_Serializer