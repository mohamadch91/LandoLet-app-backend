from django.db import models

from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from django.core.validators import RegexValidator

class User(AbstractUser):
    username = models.CharField( null=True,unique=True,max_length=20,blank=True)
    phoneNumberRegex = RegexValidator(regex = r"^\+?98?\d{8,10}$")
    phone = models.CharField(validators = [phoneNumberRegex], max_length = 13, unique = True)
    email=models.EmailField(_('email address'),blank=True)
    title = models.CharField(max_length=5,blank=True,null=True)
    birth = models.DateField(blank=True,null=True)
    address = models.CharField(max_length=255,blank=True,null=True)
    city = models.CharField(max_length=50,blank=True,null=True)
    zip = models.CharField(max_length=5,blank=True,null=True)
    USERNAME_FIELD='phone'
    REQUIRED_FIELDS = ['username','email', 'first_name', 'last_name']
    def __str__(self):
        return "{}".format(self.phone)


