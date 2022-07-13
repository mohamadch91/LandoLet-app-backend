# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Apiservices(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
    regdate = models.CharField(db_column='RegDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    controller = models.TextField(db_column='Controller', blank=True, null=True)  # Field name made lowercase.
    view = models.TextField(db_column='View', blank=True, null=True)  # Field name made lowercase.
    text = models.TextField(db_column='Text', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'APIServices'


class Apiservicesinrole(models.Model):
    roleid = models.ForeignKey('Roles', models.DO_NOTHING, db_column='RoleId', primary_key=True)  # Field name made lowercase.
    servicesid = models.IntegerField(db_column='ServicesId')  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
    regdate = models.CharField(db_column='RegDate', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'APIServicesInRole'
        unique_together = (('roleid', 'roleid', 'servicesid'),)


class Entities(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
    regdate = models.CharField(db_column='RegDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    parentid = models.ForeignKey('self', models.DO_NOTHING, db_column='ParentId', blank=True, null=True)  # Field name made lowercase.
    sort = models.IntegerField(db_column='Sort')  # Field name made lowercase.
    dropdown = models.BooleanField(db_column='DropDown')  # Field name made lowercase.
    controller = models.TextField(db_column='Controller', blank=True, null=True)  # Field name made lowercase.
    view = models.TextField(db_column='View', blank=True, null=True)  # Field name made lowercase.
    text = models.TextField(db_column='Text', blank=True, null=True)  # Field name made lowercase.
    imageurl = models.TextField(db_column='ImageUrl', blank=True, null=True)  # Field name made lowercase.
    englishtext = models.TextField(db_column='EnglishText', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Entities'


class Entitiesinapiservices(models.Model):
    servicesid = models.ForeignKey(Apiservices, models.DO_NOTHING, db_column='ServicesId', primary_key=True)  # Field name made lowercase.
    entitiesid = models.ForeignKey(Entities, models.DO_NOTHING, db_column='EntitiesId')  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
    regdate = models.CharField(db_column='RegDate', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EntitiesInAPIServices'
        unique_together = (('servicesid', 'entitiesid'),)


class Entitiesinrole(models.Model):
    roleid = models.ForeignKey('Roles', models.DO_NOTHING, db_column='RoleId', primary_key=True)  # Field name made lowercase.
    entitiesid = models.ForeignKey(Entities, models.DO_NOTHING, db_column='EntitiesId')  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
    regdate = models.CharField(db_column='RegDate', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EntitiesInRole'
        unique_together = (('roleid', 'entitiesid'),)


class Furnitures(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
    regdate = models.CharField(db_column='RegDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    roomtypesid = models.ForeignKey('Roomtypes', models.DO_NOTHING, db_column='RoomTypesId')  # Field name made lowercase.
    furniture = models.TextField(db_column='Furniture', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Furnitures'


class Furnituresinrooms(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
    regdate = models.CharField(db_column='RegDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    furnituresid = models.ForeignKey(Furnitures, models.DO_NOTHING, db_column='FurnituresId')  # Field name made lowercase.
    roomsid = models.ForeignKey('Rooms', models.DO_NOTHING, db_column='RoomsId')  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FurnituresInRooms'


class Furnituresinroomspictures(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
    regdate = models.CharField(db_column='RegDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    furnituresinroomsid = models.ForeignKey(Furnituresinrooms, models.DO_NOTHING, db_column='FurnituresInRoomsId')  # Field name made lowercase.
    url = models.TextField(db_column='URL', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FurnituresInRoomsPictures'


class Keys(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
    regdate = models.CharField(db_column='RegDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    types = models.TextField(db_column='Types', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Keys'


class Log(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
    regdate = models.CharField(db_column='RegDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    remoteipadress = models.TextField(db_column='RemoteIPAdress', blank=True, null=True)  # Field name made lowercase.
    path = models.TextField(db_column='Path', blank=True, null=True)  # Field name made lowercase.
    querystring = models.TextField(db_column='QueryString', blank=True, null=True)  # Field name made lowercase.
    method = models.TextField(db_column='Method', blank=True, null=True)  # Field name made lowercase.
    payload = models.TextField(db_column='Payload', blank=True, null=True)  # Field name made lowercase.
    response = models.TextField(db_column='Response', blank=True, null=True)  # Field name made lowercase.
    responsecode = models.TextField(db_column='ResponseCode', blank=True, null=True)  # Field name made lowercase.
    requestedon = models.DateTimeField(db_column='RequestedOn')  # Field name made lowercase.
    respondedon = models.DateTimeField(db_column='RespondedOn')  # Field name made lowercase.
    issuccessstatuscode = models.BooleanField(db_column='IsSuccessStatusCode')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Log'


class Meterreading(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
    regdate = models.CharField(db_column='RegDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    propertiesid = models.ForeignKey('Properties', models.DO_NOTHING, db_column='PropertiesId')  # Field name made lowercase.
    meterstypesid = models.ForeignKey('Meterstypes', models.DO_NOTHING, db_column='MetersTypesId')  # Field name made lowercase.
    metervalue = models.TextField(db_column='MeterValue', blank=True, null=True)  # Field name made lowercase.
    pictureurl = models.TextField(db_column='PictureURL', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MeterReading'


class Meterstypes(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
    regdate = models.CharField(db_column='RegDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    meters = models.TextField(db_column='Meters', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MetersTypes'


class Properties(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
    regdate = models.CharField(db_column='RegDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    propertytypesid = models.ForeignKey('Propertytypes', models.DO_NOTHING, db_column='PropertyTypesId')  # Field name made lowercase.
    usersownerid = models.ForeignKey('Users', models.DO_NOTHING, db_column='UsersOwnerId')  # Field name made lowercase.
    userslandlordid = models.ForeignKey('Users', models.DO_NOTHING, db_column='UsersLandlordId')  # Field name made lowercase.
    userstenantid = models.ForeignKey('Users', models.DO_NOTHING, db_column='UsersTenantId')  # Field name made lowercase.
    postalcode = models.TextField(db_column='PostalCode', blank=True, null=True)  # Field name made lowercase.
    fulladdress = models.TextField(db_column='FullAddress', blank=True, null=True)  # Field name made lowercase.
    condition = models.IntegerField(db_column='Condition')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Properties'


class Propertykeys(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
    regdate = models.CharField(db_column='RegDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    propertiesid = models.ForeignKey(Properties, models.DO_NOTHING, db_column='PropertiesId')  # Field name made lowercase.
    keysid = models.ForeignKey(Keys, models.DO_NOTHING, db_column='KeysId')  # Field name made lowercase.
    pictureurl = models.TextField(db_column='PictureURL', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PropertyKeys'


class Propertytypes(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
    regdate = models.CharField(db_column='RegDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    types = models.TextField(db_column='Types', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PropertyTypes'

#added to data base

class Roles(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
    regdate = models.CharField(db_column='RegDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    rolename = models.TextField(db_column='RoleName', blank=True, null=True)  # Field name made lowercase.
    comments = models.TextField(db_column='Comments', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Roles'

 
class Roompictures(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
    regdate = models.CharField(db_column='RegDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    roomsid = models.ForeignKey('Rooms', models.DO_NOTHING, db_column='RoomsId')  # Field name made lowercase.
    url = models.TextField(db_column='URL', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RoomPictures'


class Roomtypes(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
    regdate = models.CharField(db_column='RegDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    types = models.TextField(db_column='Types', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RoomTypes'


class Rooms(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
    regdate = models.CharField(db_column='RegDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    roomtypesid = models.ForeignKey(Roomtypes, models.DO_NOTHING, db_column='RoomTypesId')  # Field name made lowercase.
    propertiesid = models.ForeignKey(Properties, models.DO_NOTHING, db_column='PropertiesId')  # Field name made lowercase.
    roomtitle = models.TextField(db_column='RoomTitle', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Rooms'

#added to data base
class Userinrole(models.Model):
    roleid = models.ForeignKey(Roles, models.DO_NOTHING, db_column='RoleId', primary_key=True)  # Field name made lowercase.
    usersid = models.ForeignKey('Users', models.DO_NOTHING, db_column='UsersId')  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
    regdate = models.CharField(db_column='RegDate', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UserInRole'
        unique_together = (('roleid', 'usersid'),)

#added to data base
class Users(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
    regdate = models.CharField(db_column='RegDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    password = models.TextField(db_column='Password')  # Field name made lowercase.
    type = models.IntegerField(db_column='Type')  # Field name made lowercase.
    username = models.TextField(db_column='Username', blank=True, null=True)  # Field name made lowercase.
    firstname = models.TextField(db_column='FirstName', blank=True, null=True)  # Field name made lowercase.
    lastname = models.TextField(db_column='LastName', blank=True, null=True)  # Field name made lowercase.
    email = models.TextField(db_column='Email', blank=True, null=True)  # Field name made lowercase.
    postalcode = models.TextField(db_column='PostalCode', blank=True, null=True)  # Field name made lowercase.
    fulladdress = models.TextField(db_column='FullAddress', blank=True, null=True)  # Field name made lowercase.
    phoneno = models.TextField(db_column='PhoneNo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Users'


class Efmigrationshistory(models.Model):
    migrationid = models.CharField(db_column='MigrationId', primary_key=True, max_length=150)  # Field name made lowercase.
    productversion = models.CharField(db_column='ProductVersion', max_length=32)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '__EFMigrationsHistory'
 # "default": {
    #     'ENGINE': 'sql_server.pyodbc',
    #     "NAME": "LandoLet",
    #     "USER": "sa",
    #     "PASSWORD": "mohamaD1380@",
    #     "HOST": "localhost",
    #     "PORT": "1433",
    #     "OPTIONS": {"driver": "ODBC Driver 17 for SQL Server", 
    #     },
    # },
