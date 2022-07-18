from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Roompictures)
admin.site.register(Roomtypes)
admin.site.register(Rooms)
admin.site.register(Furnitures)
admin.site.register(Furnituresinrooms)
admin.site.register(Furnituresinroomspictures)