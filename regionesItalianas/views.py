from django.http import HttpResponse   
from regionesItalianas.models import Region, Provincia
from regionesItalianas.serializers import *
from Italia.internos import json_response

# Create your views here.

def regiones(request):
    if request.method == 'GET':
        regionesLista = Region.objects.all()
        respuesta = RegionSerializer(instance=regionesLista, many=True).data
        return HttpResponse(json_response(respuesta), status=200, content_type="application/json")

def region(request, id_region):
    if request.method == 'GET':
        region = Region.objects.get(idRegion = id_region)
        respuesta = RegionSerializer(instance=region).data
        return HttpResponse(json_response(respuesta), status=200, content_type="application/json")

def provincias_region(request, id_region):
    if request.method == 'GET':
        provinciasLista = Provincia.objects.filter(region = id_region)
        respuesta = ProvinciaSerializer(instance=provinciasLista, many=True).data
        return HttpResponse(json_response(respuesta), status=200, content_type="application/json")