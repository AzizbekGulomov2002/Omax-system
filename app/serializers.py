from rest_framework import serializers
from .models import Import,Export,Buyurtma,Mijoz

class ImportSerializers(serializers.ModelSerializer):
    class Meta:
        model = Import
        fields = "__all__"
        
        
class ExportSerializers(serializers.ModelSerializer):
    class Meta:
        model = Export
        fields = "__all__"
        
        
class MijozSerializers(serializers.ModelSerializer):
    class Meta:
        model = Mijoz
        fields = "__all__"
        
class BuyurtmaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Buyurtma
        fields = "__all__"