import json
from os import stat
from urllib import response
from django.shortcuts import render

# Create your views here.
from .serializers import ChangePasswordSerializer,UpdateUserSerializer,UserSerializer
from rest_framework.permissions import AllowAny

from authen.models import User
from .serializers import RegisterSerializer,MyTokenObtainPairSerializer
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
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
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
        res={
            "first_name":serializer.data["first_name"],
            "last_name":serializer.data["last_name"],
            "email":serializer.data["email"],
            "phone":serializer.data["phone_no"],
            "postal_code":serializer.data["postal_code"],
        }
        return Response(data=serializer.data,status=status.HTTP_200_OK)