from django.shortcuts import render

# Create your views here.
import json
from os import stat
from urllib import response
from django.shortcuts import render

# Create your views here.
from .serializers import *
from rest_framework.permissions import AllowAny

from authen.models import User
from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
class registerPropertyTypeview(generics.CreateAPIView):

    permission_classes = (AllowAny,)
    serializer_class = propertyTypeSerializer
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
class PropertyTypeView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny,)
    queryset = Propertytypes.objects.all()
    serializer_class = propertyTypeSerializer
    # lookup_field = 'id'
    # lookup_field = 'id'
    def get(self, request, *args, **kwargs):
        id=request.query_params.get('id')
        if(id):
            queryset = self.queryset.all().filter(id=id)
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data)
        else:    
            serializers = self.serializer_class(self.get_queryset(), many=True)
            return Response(data=serializers.data,status=status.HTTP_200_OK)
    def put(self, request, *args, **kwargs):
        id=request.query_params.get('id')

        if(id):
            queryset=self.queryset.all().filter(id=id).first()
            serializer = self.serializer_class(queryset, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, *args, **kwargs):
           id=request.query_params.get('id')
           if(id):
                queryset=self.queryset.all().filter(id=id).first()
                serializer = self.serializer_class(queryset, data=request.data)
                serializer.is_valid(raise_exception=True)
                queryset.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
           else:
                return Response(status=status.HTTP_400_BAD_REQUEST)       
class  registerPropertyview(generics.CreateAPIView):

    permission_classes = (AllowAny,)
    serializer_class = propertySerilizer
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)        
class PropertyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny,)
    queryset = Properties.objects.all()
    serializer_class = propertySerilizer
    # lookup_field = 'id'
    # lookup_field = 'id'
    def get(self, request, *args, **kwargs):
        id=request.query_params.get('id')
        if(id):
            queryset = self.queryset.all().filter(id=id)
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data)
        else:    
            serializers = self.serializer_class(self.get_queryset(), many=True)
            return Response(data=serializers.data,status=status.HTTP_200_OK)
    def put(self, request, *args, **kwargs):
        id=request.query_params.get('id')

        if(id):
            queryset=self.queryset.all().filter(id=id).first()
            serializer = self.serializer_class(queryset, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, *args, **kwargs):
           id=request.query_params.get('id')
           if(id):
                queryset=self.queryset.all().filter(id=id).first()
                serializer = self.serializer_class(queryset, data=request.data)
                serializer.is_valid(raise_exception=True)
                queryset.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
           else:
                return Response(status=status.HTTP_400_BAD_REQUEST)  
class registerkeysview(generics.CreateAPIView):

    permission_classes = (AllowAny,)
    serializer_class = keySerilizer
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
class KeyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny,)
    queryset = Keys.objects.all()
    serializer_class = keySerilizer
    lookup_field = 'id'
    # lookup_field = 'id'
    def get(self, request, *args, **kwargs):
        id=request.query_params.get('id')
        if(id):
            queryset = self.queryset.all().filter(id=id)
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data)
        else:    
            serializers = self.serializer_class(self.get_queryset(), many=True)
            return Response(data=serializers.data,status=status.HTTP_200_OK)
    def put(self, request, *args, **kwargs):
        id=request.query_params.get('id')

        if(id):
            queryset=self.queryset.all().filter(id=id).first()
            serializer = self.serializer_class(queryset, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, *args, **kwargs):
           id=request.query_params.get('id')
           if(id):
                queryset=self.queryset.all().filter(id=id).first()
                serializer = self.serializer_class(queryset, data=request.data)
                serializer.is_valid(raise_exception=True)
                queryset.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
           else:
                return Response(status=status.HTTP_400_BAD_REQUEST)     
class registerPropertyKeysview(generics.CreateAPIView):

    permission_classes = (AllowAny,)
    serializer_class = propertyKeysSerializer
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
class PropertyKeysView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny,)
    queryset = Propertykeys.objects.all()
    serializer_class = propertyKeysSerializer
    lookup_field = 'id'
    # lookup_field = 'id'
    def get(self, request, *args, **kwargs):
        id=request.query_params.get('id')
        if(id):
            queryset = self.queryset.all().filter(id=id)
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data)
        else:    
            serializers = self.serializer_class(self.get_queryset(), many=True)
            return Response(data=serializers.data,status=status.HTTP_200_OK)
    def put(self, request, *args, **kwargs):
        id=request.query_params.get('id')

        if(id):
            queryset=self.queryset.all().filter(id=id).first()
            serializer = self.serializer_class(queryset, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, *args, **kwargs):
           id=request.query_params.get('id')
           if(id):
                queryset=self.queryset.all().filter(id=id).first()
                serializer = self.serializer_class(queryset, data=request.data)
                serializer.is_valid(raise_exception=True)
                queryset.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
           else:
                return Response(status=status.HTTP_400_BAD_REQUEST)      
class registerMeterTypesview(generics.CreateAPIView):

    permission_classes = (AllowAny,)
    serializer_class = MeterTypeSerializer
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)   
class MeterTypeView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny,)
    queryset = Meterstypes.objects.all()
    serializer_class = MeterTypeSerializer
    # lookup_field = 'id'
    def get(self, request, *args, **kwargs):
        id=request.query_params.get('id')
        if(id):
            queryset = self.queryset.all().filter(id=id)
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data)
        else:    
            serializers = self.serializer_class(self.get_queryset(), many=True)
            return Response(data=serializers.data,status=status.HTTP_200_OK)
    def put(self, request, *args, **kwargs):
        id=request.query_params.get('id')

        if(id):
            queryset=self.queryset.all().filter(id=id).first()
            serializer = self.serializer_class(queryset, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, *args, **kwargs):
           id=request.query_params.get('id')
           if(id):
                queryset=self.queryset.all().filter(id=id).first()
                serializer = self.serializer_class(queryset, data=request.data)
                serializer.is_valid(raise_exception=True)
                queryset.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
           else:
                return Response(status=status.HTTP_400_BAD_REQUEST)                         
class registerMeterReadingview(generics.CreateAPIView):

    permission_classes = (AllowAny,)
    serializer_class = MeterreadingSerializer
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)        
class MeterReadingView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny,)
    queryset = Meterreading.objects.all()
    serializer_class = MeterreadingSerializer
    lookup_field = 'id'
    # lookup_field = 'id'
    def get(self, request, *args, **kwargs):
        id=request.query_params.get('id')
        if(id):
            queryset = self.queryset.all().filter(id=id)
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data)
        else:    
            serializers = self.serializer_class(self.get_queryset(), many=True)
            return Response(data=serializers.data,status=status.HTTP_200_OK)
    def put(self, request, *args, **kwargs):
        id=request.query_params.get('id')

        if(id):
            queryset=self.queryset.all().filter(id=id).first()
            serializer = self.serializer_class(queryset, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, *args, **kwargs):
           id=request.query_params.get('id')
           if(id):
                queryset=self.queryset.all().filter(id=id).first()
                serializer = self.serializer_class(queryset, data=request.data)
                serializer.is_valid(raise_exception=True)
                queryset.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
           else:
                return Response(status=status.HTTP_400_BAD_REQUEST)  