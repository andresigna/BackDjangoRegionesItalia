from rest_framework import serializers
from regionesItalianas.models import *

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('idRegion', 'nombre', 'capital', 'poblacion', 'superficie')

class ProvinciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provincia
        fields = ('idProvincia', 'nombre', 'region')