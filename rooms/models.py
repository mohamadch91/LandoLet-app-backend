from django.db import models
from props.models import Properties
# Create your models here.


class Roompictures(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
    regdate = models.DateField(db_column='RegDate', blank=True, null=True)  # Field name made lowercase.
    roomsid = models.ForeignKey('Rooms', models.DO_NOTHING, db_column='RoomsId')  # Field name made lowercase.
    url = models.ImageField(db_column='URL', blank=True, null=True)  # Field name made lowercase.

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
    url = models.ImageField(db_column='URL', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'FurnituresInRoomsPictures'

