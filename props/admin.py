from django.contrib import admin
from .models import Keys,Meterreading,Properties,Meterstypes,Propertykeys,Propertytypes
# Register your models here.
admin.site.register(Keys)
admin.site.register(Meterreading)
admin.site.register(Properties)
admin.site.register(Meterstypes)
admin.site.register(Propertykeys)
admin.site.register(Propertytypes)
