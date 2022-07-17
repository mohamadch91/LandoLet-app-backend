from rest_framework import serializers
from .models import *
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class propertyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Propertytypes
        fields = '__all__'
        read_only_fields = ('id',)
        extra_kwargs = {
            'name': {
                'validators': [UniqueValidator(queryset=Propertytypes.objects.all())]
            }
        }

class propertySerilizer(serializers.ModelSerializer):
    class Meta:
        model = Properties
        fields = '__all__'
        read_only_fields = ('id',)
        extra_kwargs = {
            'name': {
                'validators': [UniqueValidator(queryset=Properties.objects.all())]
            }
        }

class keySerilizerview(serializers.ModelSerializer):
    class Meta:
        model = Keys
        fields = '__all__'
        read_only_fields = ('id',)
        extra_kwargs = {
            'name': {
                'validators': [UniqueValidator(queryset=Keys.objects.all())]
            }
        }
class propertyKeysSerializerview(serializers.ModelSerializer):
    class Meta:
        model = Propertykeys
        fields = '__all__'
        read_only_fields = ('id',)
        extra_kwargs = {
            'name': {
                'validators': [UniqueValidator(queryset=Propertykeys.objects.all())]
            }
        }        