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
    id = models.AutoField(db_column='Id', primary_key=True,db_index=True)   
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)   
    types = models.TextField(db_column='Types', blank=True, null=True,db_index=True)   

    class Meta:
        # managed = False
        db_table = 'Keys'



class Meterreading(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)   
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)   
    propertiesid = models.ForeignKey('Properties', models.CASCADE, db_column='PropertiesId',db_index=True)   
    meterstypesid = models.ForeignKey('Meterstypes', models.CASCADE, db_column='MetersTypesId',db_index=True)   
    metervalue = models.TextField(db_column='MeterValue', blank=True, null=True)   
    pictureurl=models.ImageField(upload_to='props/meters/',db_column='PictureURL', blank=True,null=True)   

    class Meta:
        # managed = False
        db_table = 'MeterReading'


class Meterstypes(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)   
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)   
    meters = models.TextField(db_column='Meters', blank=True, null=True,db_index=True)   
    is_default = models.BooleanField(db_column='IsDefault',blank=True ,null=True,db_index=True)
    user_id=models.ForeignKey(settings.AUTH_USER_MODEL,db_column='userId',on_delete= models.CASCADE,blank=True,null=True,db_index=True)

    class Meta:
        # managed = False
        db_table = 'MetersTypes'


class Properties(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)   
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)   
    propertytypesid = models.ForeignKey('Propertytypes', models.CASCADE, db_column='PropertyTypesId',db_index=True)   
    usersownerid = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE, db_column='UsersOwnerId',related_name='User_owner_id',blank=True,null=True,db_index=True)   
    userslandlordid = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE, db_column='UsersLandlordId',related_name='User_landlord_id',blank=True,null=True,db_index=True)   
    userstenantid = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE, db_column='UsersTenantId',related_name='User_tenant_id',blank=True,null=True,db_index=True)   
    postalcode = models.TextField(db_column='PostalCode', blank=True, null=True)   
    fulladdress = models.TextField(db_column='FullAddress', blank=True, null=True)   
    status = models.IntegerField(db_column='status',db_index=True,default=0)   
    condition = models.IntegerField(db_column='Condition',db_index=True,default=0)
    signature=models.ImageField(upload_to='props/signatures/',db_column='Signature', blank=True,null=True)
    signature_name=models.CharField(max_length=100,db_column='SignatureName', blank=True,null=True)
    class Meta:
        # managed = False
        db_table = 'Properties'


class Propertykeys(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)   
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)   
    propertiesid = models.ForeignKey(Properties, models.CASCADE, db_column='PropertiesId',db_index=True)   
    keysid = models.ForeignKey(Keys, models.CASCADE, db_column='KeysId',db_index=True)   
    count=models.IntegerField(db_column='Count',blank=True,null=True)
    # pictureurl=models.ImageField(upload_to='props/',db_column='PictureURL', blank=True,null=True)   

    class Meta:
        # managed = False
        db_table = 'PropertyKeys'


class Propertytypes(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True,db_index=True)   
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)   
    types = models.TextField(db_column='Types', blank=True, null=True,db_index=True)   
    # pictureurl=models.ImageField(upload_to='props/',db_column='PictureURL', blank=True,null=True)
    class Meta:
        # managed = False
        db_table = 'PropertyTypes'


class PropertyComment(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)   
    property_id=models.ForeignKey(Properties,db_column="PropertyId",blank=True,null=True,on_delete=models.CASCADE,db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)   
    comment=models.TextField(db_column="Comment",blank=True,null=True,db_index=True)
    class Meta:
        db_table = 'PropertyComment'
    