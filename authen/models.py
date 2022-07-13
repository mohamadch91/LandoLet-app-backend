from django.db import models

from django.contrib.auth.models import AbstractUser

class Roles(models.Model):
    class Role(models.TextChoices):
        TENANT="Tenant"
        LANLORD="Landlord"
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
    regdate = models.CharField(db_column='RegDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    rolename = models.TextField(db_column='RoleName', blank=True, null=True,choices=Role.choices)  # Field name made lowercase.
    comments = models.TextField(db_column='Comments', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'Roles'


class User(AbstractUser):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive',default=False)  # Field name made lowercase.
    regdate = models.CharField(db_column='RegDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    password = models.TextField(db_column='Password')  # Field name made lowercase.
    type = models.IntegerField(db_column='Type',default=0)  # Field name made lowercase.
    # username = models.TextField(db_column='Username', blank=True, null=True)  # Field name made lowercase.
    firstname = models.TextField(db_column='FirstName', blank=True, null=True)  # Field name made lowercase.
    lastname = models.TextField(db_column='LastName', blank=True, null=True)  # Field name made lowercase.
    email = models.TextField(db_column='Email',unique=True, blank=True, null=True)  # Field name made lowercase.
    postalcode = models.TextField(db_column='PostalCode', blank=True, null=True)  # Field name made lowercase.
    fulladdress = models.TextField(db_column='FullAddress', blank=True, null=True)  # Field name made lowercase.
    phoneno = models.TextField(db_column='PhoneNo', blank=True, null=True)  # Field name made lowercase.
    USERNAME_FIELD='email'
    REQUIRED_FIELDS = ['username', 'password', 'postalcode','phoneno','type']
    class Meta:
        # managed = False
        db_table = 'Users'
 

class Userinrole(models.Model):
    roleid = models.ForeignKey(Roles, models.DO_NOTHING, db_column='RoleId', primary_key= True)  # Field name made lowercase.
    usersid = models.ForeignKey(User, models.DO_NOTHING, db_column='UsersId')  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
    regdate = models.CharField(db_column='RegDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    
    class Meta:
        # managed = False
        db_table = 'UserInRole'
        unique_together = (('roleid', 'usersid'),)


