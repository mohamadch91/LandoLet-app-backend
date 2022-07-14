
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from authen.models import User, Roles, Userinrole
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

import json
class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = ['role_name','isactive']

    def create(self, validated_data):
        role = Roles.objects.create(**validated_data)
        return role



 ## define the serializer class for Ueser model    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','is_active','username','password','firstname','lastname','phoneno','fulladdress','type','postalcode','regdate',]
        extra_kwargs = {'password': {'write_only': True}}

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    usersid=UserSerializer()
    roleid=RoleSerializer()   
    class Meta:
        model = Userinrole
        fields = ['usersid','roleid']
        extra_kwargs = {'usersid': {'required': True}, 'roleid': {'required': True}}
    def create(self, validated_data):
      
        temp=json.dumps(validated_data['usersid'])
        # print(temp)
        usersid = User.objects.create_user(**validated_data['usersid'])
        # usersid.save()
        roleid = Roles.objects.create(role_name=validated_data['roleid']['role_name'],isactive=validated_data['roleid']['isactive'],regdate=validated_data['usersid']['regdate'])
        # roleid.save()
        userinrole = Userinrole.objects.create(usersid=usersid,roleid=roleid,regdate=usersid.regdate,isactive=roleid.isactive)
        # print(userinrole.roleid.id)
        return userinrole       

# user update serilizer         
class UpdateUserSerializer(serializers.ModelSerializer):
    username=serializers.CharField(validators=[UniqueValidator(queryset=User.objects.all())])
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
        }

    def validate_email(self, value):
        user = self.context['request'].user
        if User.objects.exclude(id=user.id).filter(email=value).exists():
            raise serializers.ValidationError({"email": "This email is already in use."})
        return value

    def validate_username(self, value):
        user = self.context['request'].user
        if User.objects.exclude(id=user.id).filter(username=value).exists():
            raise serializers.ValidationError({"username": "This username is already in use."})
        return value
    def validate_postal_code(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("Postal code must be numeric.")
        return value
    def validate_phone_number(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("Phone number must be numeric.")
        return value        
    
    def update(self, instance, validated_data):
        instance=super().update(instance, validated_data)
        instance.save()
        return instance    
# user change password serializer
class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('old_password', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError({"old_password": "Old password is not correct"})
        return value

    def update(self, instance, validated_data):

        instance.set_password(validated_data['password'])
        instance.save()

        return instance      
 