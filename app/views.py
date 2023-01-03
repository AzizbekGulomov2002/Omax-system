from django.shortcuts import render

# Create your views he

from rest_framework.viewsets import ModelViewSet
from .serializers import ImportSerializers,ExportSerializers,MijozSerializers,BuyurtmaSerializers
from .models import Import, Export, Mijoz, Buyurtma


class ImportViewSet(ModelViewSet):
    queryset = Import.objects.all()
    serializer_class = ImportSerializers
    http_method_names = ['get','head']
    
    
    
class ExportViewSet(ModelViewSet):
    queryset = Export.objects.all()
    serializer_class = ExportSerializers
    http_method_names = ['get','head']
    
    
class MijozViewSet(ModelViewSet):
    queryset = Mijoz.objects.all()
    serializer_class = MijozSerializers
    http_method_names = ['get','head']
    
class BuyurtmaViewSet(ModelViewSet):
    queryset = Buyurtma.objects.all()
    serializer_class = BuyurtmaSerializers
    http_method_names = ['get','head']