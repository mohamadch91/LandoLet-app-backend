
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

class keySerilizer(serializers.ModelSerializer):
    class Meta:
        model = Keys
        fields = '__all__'
        read_only_fields = ('id',)
        extra_kwargs = {
            'name': {
                'validators': [UniqueValidator(queryset=Keys.objects.all())]
            }
        }
class propertyKeysSerializer(serializers.ModelSerializer):
    class Meta:
        model = Propertykeys
        fields = '__all__'
        read_only_fields = ('id',)
        extra_kwargs = {
            'name': {
                'validators': [UniqueValidator(queryset=Propertykeys.objects.all())]
            }
        }  

class MeterTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meterstypes
        fields = '__all__'
        read_only_fields = ('id',)
        extra_kwargs = {
            'name': {
                'validators': [UniqueValidator(queryset=Meterstypes.objects.all())]
            }
        }

class MeterreadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meterreading
        fields = '__all__'
        read_only_fields = ('id',)
        extra_kwargs = {
            'name': {
                'validators': [UniqueValidator(queryset=Meterreading.objects.all())]
            }
        }        
class PropertyStatusSerilizer(serializers.ModelSerializer):
    class Meta:
        model = PropertyStatus
        fields = '__all__'
        read_only_fields = ('id',)
        extra_kwargs = {
            'name': {
                'validators': [UniqueValidator(queryset=PropertyStatus.objects.all())]
            }
        }        