from rest_framework.viewsets import ModelViewSet
from .serializers import *

class Member_View(ModelViewSet):
    queryset=Member.objects.all()
    serializer_class=Member_Serializer

    def list(self, request, *args, **kwargs):
        print(kwargs)
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)