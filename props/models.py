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

class Furnitures(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
    regdate = models.DateField(db_column='RegDate', blank=True, null=True)  # Field name made lowercase.
    roomtypesid = models.ForeignKey('Roomtypes', models.DO_NOTHING, db_column='RoomTypesId')  # Field name made lowercase.
    furniture = models.TextField(db_column='Furniture', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'Furnitures'


class Furnituresinrooms(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
    regdate = models.DateField(db_column='RegDate', blank=True, null=True)  # Field name made lowercase.
    furnituresid = models.ForeignKey(Furnitures, models.DO_NOTHING, db_column='FurnituresId')  # Field name made lowercase.
    roomsid = models.ForeignKey('Rooms', models.DO_NOTHING, db_column='RoomsId')  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity')  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'FurnituresInRooms'


class Furnituresinroomspictures(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
    regdate = models.DateField(db_column='RegDate', blank=True, null=True)  # Field name made lowercase.
    furnituresinroomsid = models.ForeignKey(Furnituresinrooms, models.DO_NOTHING, db_column='FurnituresInRoomsId')  # Field name made lowercase.
    url = models.TextField(db_column='URL', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'FurnituresInRoomsPictures'


class Keys(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
    regdate = models.DateField(db_column='RegDate', blank=True, null=True)  # Field name made lowercase.
    types = models.TextField(db_column='Types', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'Keys'



class Meterreading(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
    regdate = models.DateField(db_column='RegDate', blank=True, null=True)  # Field name made lowercase.
    propertiesid = models.ForeignKey('Properties', models.DO_NOTHING, db_column='PropertiesId')  # Field name made lowercase.
    meterstypesid = models.ForeignKey('Meterstypes', models.DO_NOTHING, db_column='MetersTypesId')  # Field name made lowercase.
    metervalue = models.TextField(db_column='MeterValue', blank=True, null=True)  # Field name made lowercase.
    pictureurl = models.TextField(db_column='PictureURL', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'MeterReading'


class Meterstypes(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
    regdate = models.DateField(db_column='RegDate', blank=True, null=True)  # Field name made lowercase.
    meters = models.TextField(db_column='Meters', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'MetersTypes'


class Properties(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
    regdate = models.DateField(db_column='RegDate', blank=True, null=True)  # Field name made lowercase.
    propertytypesid = models.ForeignKey('Propertytypes', models.DO_NOTHING, db_column='PropertyTypesId')  # Field name made lowercase.
    usersownerid = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='UsersOwnerId',related_name='User_owner_id')  # Field name made lowercase.
    userslandlordid = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='UsersLandlordId',related_name='User_landlord_id')  # Field name made lowercase.
    userstenantid = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='UsersTenantId',related_name='User_tenant_id')  # Field name made lowercase.
    postalcode = models.TextField(db_column='PostalCode', blank=True, null=True)  # Field name made lowercase.
    fulladdress = models.TextField(db_column='FullAddress', blank=True, null=True)  # Field name made lowercase.
    condition = models.IntegerField(db_column='Condition')  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'Properties'


class Propertykeys(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
    regdate = models.DateField(db_column='RegDate', blank=True, null=True)  # Field name made lowercase.
    propertiesid = models.ForeignKey(Properties, models.DO_NOTHING, db_column='PropertiesId')  # Field name made lowercase.
    keysid = models.ForeignKey(Keys, models.DO_NOTHING, db_column='KeysId')  # Field name made lowercase.
    pictureurl = models.TextField(db_column='PictureURL', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'PropertyKeys'


class Propertytypes(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
    regdate = models.DateField(db_column='RegDate', blank=True, null=True)  # Field name made lowercase.
    types = models.TextField(db_column='Types', blank=True, null=True)  # Field name made lowercase.
    image=models.ImageField(upload_to='media/',db_column='Image'    , blank=True,null=True)
    class Meta:
        # managed = False
        db_table = 'PropertyTypes'



class Roompictures(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
    regdate = models.DateField(db_column='RegDate', blank=True, null=True)  # Field name made lowercase.
    roomsid = models.ForeignKey('Rooms', models.DO_NOTHING, db_column='RoomsId')  # Field name made lowercase.
    url = models.TextField(db_column='URL', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'RoomPictures'


class Roomtypes(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
    regdate = models.DateField(db_column='RegDate', blank=True, null=True)  # Field name made lowercase.
    types = models.TextField(db_column='Types', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'RoomTypes'


class Rooms(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
    regdate = models.DateField(db_column='RegDate', blank=True, null=True)  # Field name made lowercase.
    roomtypesid = models.ForeignKey(Roomtypes, models.DO_NOTHING, db_column='RoomTypesId')  # Field name made lowercase.
    propertiesid = models.ForeignKey(Properties, models.DO_NOTHING, db_column='PropertiesId')  # Field name made lowercase.
    roomtitle = models.TextField(db_column='RoomTitle', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'Rooms'
