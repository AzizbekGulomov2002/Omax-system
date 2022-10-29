from rest_framework import serializers
from .models import Zakas

class ZakasSerializers(serializers.ModelSerializer):
    class Meta:
        model = Zakas
        fields = "__all__"
        