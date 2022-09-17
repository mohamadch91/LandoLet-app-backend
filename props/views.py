from re import I
from django.shortcuts import render

# Create your views here.
import json
from os import stat
from urllib import response
from django.shortcuts import render

# Create your views here.
from .serializers import *
from rest_framework.permissions import IsAuthenticated

from authen.models import User
from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
class registerPropertyTypeview(generics.CreateAPIView):

    permission_classes = (IsAuthenticated,)
    serializer_class = propertyTypeSerializer
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
class PropertyTypeView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
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

    permission_classes = (IsAuthenticated,)
    serializer_class = propertySerilizer
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)        
class PropertyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
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

    permission_classes = (IsAuthenticated,)
    serializer_class = keySerilizer
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
class KeyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
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
        if(id is not None):
            queryset=self.queryset.all().filter(id=id).first()
            serializer = self.serializer_class(queryset, data=request.data)
            if(serializer.is_valid()):
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message":"need query params"},status=status.HTTP_400_BAD_REQUEST)
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

    permission_classes = (IsAuthenticated,)
    serializer_class = propertyKeysSerializer
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
class PropertyKeysView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
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
class registerMeterTypesview(APIView):
    permission_classes = (IsAuthenticated,)
    # serializer_class=MeterTypeSerializer
    def post(self, request):
        serializer = MeterTypeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        x=Meterstypes.objects.create(user_id=request.user,isactive=request.data['isactive'],regdate=request.data['regdate'],is_default=request.data['is_default'],meters=request.data['meters'])
        ser=MeterTypeSerializer(x)
        return Response(ser.data, status=status.HTTP_201_CREATED)   


class MeterTypeView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
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
            
            queryset=self.queryset.all().filter(user_id=request.user)
            q1=self.queryset.filter(is_default=True)
            x=MeterTypeSerializer(q1,many=True)
            y=MeterTypeSerializer(queryset,many=True)
            z=x.data+y.data

            return Response(data=z,status=status.HTTP_200_OK)
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

    permission_classes = (IsAuthenticated,)
    serializer_class = MeterreadingSerializer
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)        
class MeterReadingView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
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