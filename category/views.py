from rest_framework.viewsets import ModelViewSet
from .serializers import *

class Category_View(ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=Category_Serializer