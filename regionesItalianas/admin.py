from django.contrib import admin

from regionesItalianas.models import Provincia, Region

# Register your models here.

admin.site.register(Region)
admin.site.register(Provincia)