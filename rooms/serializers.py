from rest_framework import serializers
from .models import *
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class RoomPictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roompictures
        fields = '__all__'
class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = '__all__'        

class RoomTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roomtypes
        fields = '__all__'
class FurnituresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Furnitures
        fields = '__all__'
class FurnituresInRoomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Furnituresinrooms
        fields = '__all__'
class FurnituresInRoomsPictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Furnituresinroomspictures
        fields = '__all__'                        