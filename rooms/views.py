from django.shortcuts import render

# Create your views here.
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

class registerRoomPictureview(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RoomPictureSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
class RoomPictureView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny,)
    queryset = Roompictures.objects.all()
    serializer_class = RoomPictureSerializer
    lookup_field = 'id'
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
class registerRoomTypesView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RoomTypesSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
class RoomTypesView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny,)
    queryset = Roomtypes.objects.all()
    serializer_class = RoomTypesSerializer
    lookup_field = 'id'
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
class registerRoomsView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RoomSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
class RooomView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny,)
    queryset = Rooms.objects.all()
    serializer_class = RoomSerializer
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

#furnitures
class registerFurnitureView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = FurnituresSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
class Furnitureview(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny,)
    queryset = Furnitures.objects.all()
    serializer_class = FurnituresSerializer
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

  #furnituures in room
class registerFurnitureInRoomView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = FurnituresInRoomsSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)      
class FurnitureInRoomView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(AllowAny,)
    queryset = Furnituresinrooms.objects.all()   
    serializer_class = FurnituresInRoomsSerializer
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

class registerFurnituresinroomspicturesView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = FurnituresInRoomsPictureSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)      
class FurnitureinroomspicturesView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(AllowAny,)
    queryset = Furnituresinroomspictures.objects.all()   
    serializer_class = FurnituresInRoomsPictureSerializer
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