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
from rest_framework.permissions import IsAuthenticated

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
import copy
class registerRoomPictureview(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = RoomPictureSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
class RoomPictureView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Roompictures.objects.all()
    serializer_class = RoomPictureSerializer
    lookup_field = 'id'
    def get(self, request, *args, **kwargs):
        id=request.query_params.get('r_id')
        if(id is not None):
            queryset = self.queryset.all().filter(roomsid=id)
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data)
        else:    
            serializers = self.serializer_class(self.get_queryset(), many=True)
            return Response(data=serializers.data,status=status.HTTP_200_OK)
    def put(self, request, *args, **kwargs):
        id=request.query_params.get('id')

        if(id is not None):
            queryset=get_object_or_404(Roompictures,id=id)
            serializer = self.serializer_class(queryset, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, *args, **kwargs):
           id=request.query_params.get('id')
           if(id is not None):
                queryset=get_object_or_404(Roompictures,id=id)
                queryset.delete()
                return Response({"message" :"delete succsessfully"},status=status.HTTP_204_NO_CONTENT)
           else:
                return Response({"message" :"need query param"},status=status.HTTP_400_BAD_REQUEST)       
class registerRoomTypesView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = RoomTypesSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
class RoomTypesView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Roomtypes.objects.all()
    serializer_class = RoomTypesSerializer
    lookup_field = 'id'
    def get(self, request, *args, **kwargs):
        id=request.query_params.get('id')
        if(id is not None):
            queryset = self.queryset.all().filter(id=id)
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data)
        else:    
            serializers = self.serializer_class(self.get_queryset(), many=True)
            return Response(data=serializers.data,status=status.HTTP_200_OK)
    def put(self, request, *args, **kwargs):
        id=request.query_params.get('id')
        if(id is not None):
            queryset=get_object_or_404(Roomtypes,id=id)
            serializer = self.serializer_class(queryset, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, *args, **kwargs):
           id=request.query_params.get('id')
           if(id is not None):
                queryset=get_object_or_404(Roomtypes,id=id)
               
                queryset.delete()
                return Response({"message" :"delete succsessfully"},status=status.HTTP_204_NO_CONTENT)
           else:
                return Response({"message" :"need query param"},status=status.HTTP_400_BAD_REQUEST)
class registerRoomsView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = RoomSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
class RooomView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Rooms.objects.all()
    serializer_class = RoomSerializer
    def get(self, request, *args, **kwargs):
        id=request.query_params.get('p_id')
        if(id is not None):
            queryset = self.queryset.filter(propertiesid=id)
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data)
        else:    
            return Response({"messsage": "need query param"},status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, *args, **kwargs):
        id=request.query_params.get('id')

        if(id  is not None):
            queryset=get_object_or_404(Rooms,id=id) 
            serializer = self.serializer_class(queryset, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, *args, **kwargs):
           id=request.query_params.get('id')
           if(id is not None):
                queryset=get_object_or_404(Rooms,id=id) 
               
                queryset.delete()
                return Response({"messsage": "Delete succsessfully"},status=status.HTTP_204_NO_CONTENT)
           else:
                return Response({"messsage": "need query param"},status=status.HTTP_400_BAD_REQUEST)       

#furnitures
class registerFurnitureView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = FurnituresSerializer
    def post(self, request):
        new_data=copy.deepcopy(request.data)
        new_data['is_active']=True
        new_data['is_default']=False
        ser=FurnituresSerializer(data=new_data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data,status=status.HTTP_201_CREATED)
        else:
            return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)
class Furnitureview(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Furnitures.objects.all()
    serializer_class = FurnituresSerializer
    def get(self, request, *args, **kwargs):
        id=request.query_params.get('r_id')
        if(id is not None):
            queryset = Furnitures.objects.filter(roomtypesid=id,user_id=request.user.id)
            queryset1 = Furnitures.objects.filter(roomtypesid=id,is_default=True)
            queryset=queryset.union(queryset1)
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data)
        else:    
           
            queryset=self.queryset.all().filter(user_id=request.user)
            q1=self.queryset.filter(is_default=True)
            x=FurnituresSerializer(q1,many=True)
            y=FurnituresSerializer(queryset,many=True)
            z=x.data+y.data
            return Response(data=z,status=status.HTTP_200_OK)
    def put(self, request, *args, **kwargs):
        id=request.query_params.get('id')

        if(id is not None):
            if(int(id)<16):
                return Response({"message" :"can not update default furniture"},status=status.HTTP_400_BAD_REQUEST)
            queryset=get_object_or_404(Furnitures,id=id)
            serializer = self.serializer_class(queryset, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({"message" :"need query param"},status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, *args, **kwargs):
           id=request.query_params.get('id')
           if(id is not None):
                if(int(id)<16):
                    return Response({"message" :"can not delete default furniture"},status=status.HTTP_400_BAD_REQUEST)
                queryset=get_object_or_404(Furnitures,id=id)
               
                queryset.delete()
                return Response({"message" :"delete succsessfully"},status=status.HTTP_204_NO_CONTENT)
           else:
                return Response({"message" :"need query param"},status=status.HTTP_400_BAD_REQUEST)       

  #furnituures in room
class registerFurnitureInRoomView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = FurnituresInRoomsSerializer
    def post(self, request):
        room=get_object_or_404(Rooms,id=request.data['roomsid'])
        furniture=get_object_or_404(Furnitures,id=request.data['furnituresid'])
        if(room.roomtypesid.id!=furniture.roomtypesid.id):
            return Response({"message" :"room and furniture are not match"},status=status.HTTP_400_BAD_REQUEST)
        ser=FurnituresInRoomsSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data,status=status.HTTP_201_CREATED)
        else:
            return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)
        
class FurnitureInRoomView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    queryset = Furnituresinrooms.objects.all()   
    serializer_class = FurnituresInRoomsSerializer
    def get(self, request, *args, **kwargs):
        id=request.query_params.get('r_id')
        if(id is not None):
            queryset = self.queryset.filter(roomsid=id)
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data)
        else:    
            serializers = self.serializer_class(self.get_queryset(), many=True)
            return Response(data=serializers.data,status=status.HTTP_200_OK)
    def put(self, request, *args, **kwargs):
        id=request.query_params.get('id')

        if(id is not None):
            queryset=get_object_or_404(Furnituresinrooms,id=id)
            serializer = self.serializer_class(queryset, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({"message" :"need query param"},status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, *args, **kwargs):
           id=request.query_params.get('id')
           if(id is not None):
                queryset=get_object_or_404(Furnituresinrooms,id=id)
                queryset.delete()
                return Response({"message" :"delete succsessfully"},status=status.HTTP_204_NO_CONTENT)
           else:
                return Response({"message" :"need query param"},status=status.HTTP_400_BAD_REQUEST)       

class registerFurnituresinroomspicturesView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = FurnituresInRoomsPictureSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)      
class FurnitureinroomspicturesView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    queryset = Furnituresinroomspictures.objects.all()   
    serializer_class = FurnituresInRoomsPictureSerializer
    def get(self, request, *args, **kwargs):
        f_id=request.query_params.get('f_id')
        r_id=request.query_params.get('r_id')
        if(f_id is not None and r_id is not None):
            return Response({"message" :"can not have both query param"},status=status.HTTP_400_BAD_REQUEST)
        if(f_id is not None):
            queryset = self.queryset.filter(furnituresinroomsid=f_id)
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data)
        if(r_id is not None):
            queryset = self.queryset.filter(furnituresinroomsid__roomsid=r_id)
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data)
    def put(self, request, *args, **kwargs):
        id=request.query_params.get('id')

        if(id is not None):
            queryset=get_object_or_404(Furnituresinroomspictures,id=id)
            serializer = self.serializer_class(queryset, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({"message" :"need query param"},status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, *args, **kwargs):
           id=request.query_params.get('id')
           if(id is not None):
                queryset=get_object_or_404(Furnituresinroomspictures,id=id)
              
                queryset.delete()
                return Response({"message" :"delete succsessfully"},status=status.HTTP_204_NO_CONTENT)
           else:
                return Response({"message" :"need query param"},status=status.HTTP_400_BAD_REQUEST)    