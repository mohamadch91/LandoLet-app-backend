from pyexpat import model
from turtle import ondrag
from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.conf import settings


class Keys(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
      # Field name made lowercase.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # Field name made lowercase.
    types = models.TextField(db_column='Types', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'Keys'



class Meterreading(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
      # Field name made lowercase.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # Field name made lowercase.
    propertiesid = models.ForeignKey('Properties', models.CASCADE, db_column='PropertiesId')  # Field name made lowercase.
    meterstypesid = models.ForeignKey('Meterstypes', models.CASCADE, db_column='MetersTypesId')  # Field name made lowercase.
    metervalue = models.TextField(db_column='MeterValue', blank=True, null=True)  # Field name made lowercase.
    pictureurl=models.ImageField(upload_to='props/',db_column='PictureURL', blank=True,null=True)  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'MeterReading'


class Meterstypes(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    # Field name made lowercase.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # Field name made lowercase.
    meters = models.TextField(db_column='Meters', blank=True, null=True)  # Field name made lowercase.
    is_default = models.BooleanField(db_column='IsDefault',blank=True ,null=True)
    user_id=models.ForeignKey(settings.AUTH_USER_MODEL,db_column='userId',on_delete= models.CASCADE,blank=True,null=True)

    class Meta:
        # managed = False
        db_table = 'MetersTypes'


class Properties(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
      # Field name made lowercase.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # Field name made lowercase.
    propertytypesid = models.ForeignKey('Propertytypes', models.CASCADE, db_column='PropertyTypesId')  # Field name made lowercase.
    usersownerid = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE, db_column='UsersOwnerId',related_name='User_owner_id',blank=True,null=True)  # Field name made lowercase.
    userslandlordid = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE, db_column='UsersLandlordId',related_name='User_landlord_id',blank=True,null=True)  # Field name made lowercase.
    userstenantid = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE, db_column='UsersTenantId',related_name='User_tenant_id',blank=True,null=True)  # Field name made lowercase.
    postalcode = models.TextField(db_column='PostalCode', blank=True, null=True)  # Field name made lowercase.
    fulladdress = models.TextField(db_column='FullAddress', blank=True, null=True)  # Field name made lowercase.
    condition = models.IntegerField(db_column='Condition')  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'Properties'


class Propertykeys(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
      # Field name made lowercase.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # Field name made lowercase.
    propertiesid = models.ForeignKey(Properties, models.CASCADE, db_column='PropertiesId')  # Field name made lowercase.
    keysid = models.ForeignKey(Keys, models.CASCADE, db_column='KeysId')  # Field name made lowercase.
    count=models.IntegerField(db_column='Count',blank=True,null=True)
    # pictureurl=models.ImageField(upload_to='props/',db_column='PictureURL', blank=True,null=True)  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'PropertyKeys'


class Propertytypes(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
      # Field name made lowercase.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # Field name made lowercase.
    types = models.TextField(db_column='Types', blank=True, null=True)  # Field name made lowercase.
    # pictureurl=models.ImageField(upload_to='props/',db_column='PictureURL', blank=True,null=True)
    class Meta:
        # managed = False
        db_table = 'PropertyTypes'

class PropertyStatus(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
      # Field name made lowercase.
    property_id=models.ForeignKey(Properties,db_column="PropertyId",blank=True,null=True,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # Field name made lowercase.
    comment=models.TextField(db_column="Comment",blank=True,null=True)
    class Meta:
        db_table = 'PropertyStatus'

class PropertyComment(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
      # Field name made lowercase.
    property_id=models.ForeignKey(Properties,db_column="PropertyId",blank=True,null=True,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # Field name made lowercase.
    comment=models.TextField(db_column="Comment",blank=True,null=True)
    class Meta:
        db_table = 'PropertyComment'
    