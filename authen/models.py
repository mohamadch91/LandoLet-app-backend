from django.db import models

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager,BaseUserManager
from django.contrib.auth.hashers import make_password

class CustomUserManager(BaseUserManager):
    """
    Custom user model manager
    """

    def create_user(self, username, password, **extra_fields):
        # print("debug")
        print(username)
        if not username:
            raise ValueError('The username must be set')

        # password=make_password(password)       
        # return self.create_user(username, password, **extra_fields)
        user = self.model(username=username, password=password, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password,email=None ,**extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(username, password, **extra_fields)




class User(AbstractUser):
    class Role(models.TextChoices):
        TENANT="Tenant"
        LANLORD="Landlord"    

    username=models.EmailField(db_column='Email',unique=True, blank=True, null=True) 
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    is_active = models.BooleanField(db_column='IsActive',default=True)  # Field name made lowercase.
    regdate = models.DateField(db_column='RegDate', blank=True, null=True)  # Field name made lowercase.
    role=models.CharField(db_column='Role_name',max_length=10,choices=Role.choices)
    # username = models.TextField(db_column='Username', blank=True, null=True)  # Field name made lowercase.
    first_name = models.TextField(db_column='FirstName', blank=True, null=True)  # Field name made lowercase.
    last_name = models.TextField(db_column='LastName', blank=True, null=True)  # Field name made lowercase.
    email =None  # Field name made lowercase.
    postal_code = models.IntegerField(db_column='PostalCode', blank=True, null=True)  # Field name made lowercase.
    full_address = models.TextField(db_column='FullAddress', blank=True, null=True)  # Field name made lowercase.
    phone_no = models.IntegerField(db_column='PhoneNo', blank=True, null=True)  # Field name made lowercase.
    class Meta:
        # managed = False
        db_table = 'Users'
    objects = CustomUserManager()
 
 

