from django.db import models
# Create your models here.

class Region(models.Model):
    idRegion = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    capital = models.CharField(max_length=30)
    poblacion = models.IntegerField()
    superficie = models.FloatField()

    def __str__(self):
        return self.nombre

class Provincia(models.Model):
    idProvincia = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    region = models.ForeignKey('Region', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

    
