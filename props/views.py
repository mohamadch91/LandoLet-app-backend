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
import copy
class RegisterPropertyTypeView(generics.CreateAPIView):

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

        if(id is not None):
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
class  RegisterPropertyView(generics.CreateAPIView):

    permission_classes = (IsAuthenticated,)
    serializer_class = propertySerilizer
    def post(self, request):
        new_data=copy.deepcopy(request.data)
        new_data['usersownerid']=request.user.id
        serializer = self.get_serializer(data=new_data)
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
        
        if(id is not None):
            queryset=self.queryset.all().filter(id=id).first()
            serializer = self.serializer_class(queryset, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, *args, **kwargs):
           id=request.query_params.get('id')
           if(id is not None):
                obj=get_object_or_404(Properties,id=id)
                obj.delete()
                return Response({
    "message": "Property deleted successfully"
    }   
,status=status.HTTP_204_NO_CONTENT)
           else:
                return Response({
    "message": "need query param"
    },status=status.HTTP_400_BAD_REQUEST)  
class RegisterKeysView(generics.CreateAPIView):

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
class RegisterPropertyKeysView(generics.CreateAPIView):

    permission_classes = (IsAuthenticated,)
    serializer_class = propertyKeysSerializer
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
class PropertyKeysView(APIView):
    permission_classes = (IsAuthenticated,)
    # lookup_field = 'id'
    def post (self,request):
        ans=[]
        Propertykeys.objects.all().delete()
        for i in request.data['keys']:
            data={
                "propertiesid":request.data['propertyid'],
                "keysid":i["keyid"],
                "count":i["count"]
            }
            serializer = propertyKeysSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            ans.append(serializer.data)
        return Response(ans,status=status.HTTP_201_CREATED)
    def get(self, request, *args, **kwargs):
        id=request.query_params.get('id')
        if(id is not None):
            queryset = Propertykeys.objects.filter(propertiesid=id)
            serializer = propertyKeysSerializer(queryset, many=True)
            return Response(serializer.data)
            
        else:    
            queryset = Propertykeys.objects.all()
            serializer = propertyKeysSerializer(queryset, many=True)
            return Response(serializer.data)
            
    
class RegisterMeterTypesView(APIView):
    permission_classes = (IsAuthenticated,)
    # serializer_class=MeterTypeSerializer
    def post(self, request):
        new_data=copy.deepcopy(request.data)
        data={
            "meters":new_data['meters'],
            "is_default":False,
            "user_id":request.user.id
        }

        serializer = MeterTypeSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


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
            
            queryset=self.queryset.filter(user_id=request.user.id)
            q1=self.queryset.filter(is_default=True)
            x=MeterTypeSerializer(q1,many=True)
            y=MeterTypeSerializer(queryset,many=True)
            z=x.data+y.data

            return Response(data=z,status=status.HTTP_200_OK)
    def put(self, request, *args, **kwargs):
        id=request.query_params.get('id')

        if(id is not None):
            if(int(id)<4):
                return Response({"message":"you can't update default meter types"},status=status.HTTP_400_BAD_REQUEST)
            
            queryset=self.queryset.all().filter(id=id).first()
            data={
            "meters":request.data['meters'],
            "is_default":False,
            "user_id":request.user.id
             }
            serializer = self.serializer_class(queryset, data=data)
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
class RegisterMeterReadingView(generics.CreateAPIView):

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
        id=request.query_params.get('p_id')
        if(id):
            meters=Meterreading.objects.filter(propertiesid=id)
            ser=MeterreadingSerializer(meters,many=True)
            return Response(ser.data)
        else:    
            return Response({"message":"need query param"},status=status.HTTP_200_OK)
    def put(self, request, *args, **kwargs):
        id=request.query_params.get('id')

        if(id is not None):
            queryset=self.queryset.all().filter(id=id).first()
            serializer = self.serializer_class(queryset, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, *args, **kwargs):
           id=request.query_params.get('id',None)
           if(id is not None):
                x=get_object_or_404(Meterreading,id=id)
                x.delete()
                return Response({"message":"Delete succesfully"},status=status.HTTP_204_NO_CONTENT)
           else:
                return Response(status=status.HTTP_400_BAD_REQUEST)  
            

class PropertyCommentView(APIView):
    permission_classes= (IsAuthenticated,)
    def get(self,request):
        p_id=request.query_params.get('id',None)
        if (p_id is None):
            return Response({"message":"Need property id to see commnets"},status=status.HTTP_400_BAD_REQUEST)
        comments=PropertyComment.objects.filter(property=p_id)
        ser=PropertyCommentSerializer(comments,many=True)
        final_ans=[]
        for x in ser.data:
            new_data=x
            new_data["email"]=get_object_or_404(User,id=x['user']).email
            final_ans.append(new_data)
        return Response(ser.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        new_data={
            "property":request.data["property"],
            "comment":request.data["comment"],
            "user":request.user.id
        }    
        serializer=PropertyCommentSerializer(data=new_data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"comment added to property"},status=status.HTTP_201_CREATED)
        return Response({"message":"Please complete data correctly "},status=status.HTTP_400_BAD_REQUEST)
    def put(self,request):
        if ("id" not in request.data):
            return Response({"message": "id is required"},status=status.HTTP_400_BAD_REQUEST)
        comment=get_object_or_404(PropertyComment,id=request.data["id"])
        comment.comment=request.data["comment"]
        comment.save()
        return Response({"message":"comment edited succesfully"},status=status.HTTP_202_ACCEPTED)
    def delete(self,request):
        if ("id" not in request.data):
            return Response({"message": "id is required"},status=status.HTTP_400_BAD_REQUEST)
        comment=get_object_or_404(PropertyComment,id=request.data["id"])
        comment.delete()
        return Response({"message":"comment deleted succesfully"},status=status.HTTP_205_RESET_CONTENT)
        
