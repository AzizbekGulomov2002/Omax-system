from django.shortcuts import render

# Create your views he

from rest_framework.viewsets import ModelViewSet
from .serializers import ZakasSerializers
from .models import Zakas


class ZakasViewSet(ModelViewSet):
    queryset = Zakas.objects.all()
    serializer_class = ZakasSerializers
    http_method_names = ['get','head']