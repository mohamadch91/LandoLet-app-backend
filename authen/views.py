import json
from os import stat
from urllib import response
from django.shortcuts import render

# Create your views here.
from .serializers import ChangePasswordSerializer,UpdateUserSerializer,UserSerializer,LogoutSerializer
from rest_framework.permissions import AllowAny

from authen.models import User
from .serializers import *
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken
class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = [AllowAny]
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            user=User.objects.get(email=request.data['email'])
            refresh = RefreshToken.for_user(user)

            ser= ObtainTokenSerializer({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'created':True
            }).data
            final_data={
                'user':UserSerializer(user).data,
                'token':ser
            }
            return Response(final_data, status=status.HTTP_201_CREATED)

        return Response({'message':serializer.errors},status=status.HTTP_400_BAD_REQUEST)
class ChangePasswordView(generics.UpdateAPIView):
    lookup_field = 'id'
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer  
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({"Password changed succesfully"}, status=status.HTTP_200_OK) 

class UpdateProfileView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    lookup_field = 'id'
    serializer_class = UpdateUserSerializer     
class LogoutView(APIView):

    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = self.request.data.get('refresh_token')
            token = RefreshToken(token=refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)    
class LogoutAllView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        tokens = OutstandingToken.objects.filter(user_id=request.user.id)
        for token in tokens:
            t, _ = BlacklistedToken.objects.get_or_create(token=token)

        return Response(status=status.HTTP_205_RESET_CONTENT)            
class UserView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
class UserPersonal(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)

        return Response(data=serializer.data,status=status.HTTP_200_OK)
class checkEmailView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        email = request.query_params.get('email')
        if(email==None):
              return Response("need email query param",status=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(email=email).exists():
            return Response('this email already exist',status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            return Response('email is ok',status=status.HTTP_200_OK)

class Getaddresses(APIView):

    def get(self, request):
        p_code=request.query_params.get('p_code',None)
        if (p_code==None):
            return Response("need p_code query param",status=status.HTTP_400_BAD_REQUEST)
        else:
            addreses=[]
            data={
                "address": "منطقه ۱۱",
                "city": "تهران",
                "p_code": "۱۲۳۴۵۶۷۸۹۱۰",
                "province": "تهران",
                "street": "خیابان شهید بهشتی"

            }
            addreses.append(data)
            addreses.append(data)
            addreses.append(data)
            addreses.append(data)
            return Response(addreses,status=status.HTTP_200_OK)