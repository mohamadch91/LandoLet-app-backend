import json
from urllib import response
from django.shortcuts import render

# Create your views here.
from .serializers import ChangePasswordSerializer,UpdateUserSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from authen.models import User
from .serializers import RegisterSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken


class RegisterView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer   
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        res_user={
            'id':user.usersid.id,
            'isactive':user.usersid.is_active,
            'username':user.usersid.username,
            'password':user.usersid.password,
            'firstname':user.usersid.firstname,
            'lastname':user.usersid.lastname,
            'phoneno':user.usersid.phoneno,
            'fulladdress':user.usersid.fulladdress,
            'type':user.usersid.type,
            'postalcode':user.usersid.postalcode,
            'regdate':user.usersid.regdate,
            'rolename':user.roleid.role_name,
            'isactive':user.roleid.isactive,
            'roleid':user.roleid.id,
        }
        response_data = {
            "user":res_user
            
        }
        # print(serializer)
        return Response(response_data, status=status.HTTP_201_CREATED)
class ChangePasswordView(generics.UpdateAPIView):
    lookup_field = 'id'
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer  
     
class UpdateProfileView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
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