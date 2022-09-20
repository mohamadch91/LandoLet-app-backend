from itertools import count
from django.db import models
from props.models import Properties
from django.conf import settings
# Create your models here.


class Roompictures(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
      # Field name made lowercase.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # Field name made lowercase.
    roomsid = models.ForeignKey('Rooms', models.CASCADE, db_column='RoomsId')  # Field name made lowercase.
    url = models.ImageField(db_column='URL', blank=True, null=True)  # Field name made lowercase.
    comment = models.TextField(db_column='Comment', blank=True, null=True)  # Field name made lowercase.
    class Meta:
        # managed = False
        db_table = 'RoomPictures'


class Roomtypes(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
      # Field name made lowercase.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # Field name made lowercase.
    types = models.TextField(db_column='Types', blank=True, null=True)  # Field name made lowercase.
    class Meta:
        # managed = False
        db_table = 'RoomTypes'


class Rooms(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
      # Field name made lowercase.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # Field name made lowercase.
    roomtypesid = models.ForeignKey(Roomtypes, models.CASCADE, db_column='RoomTypesId',blank=True,null=True)  # Field name made lowercase.
    propertiesid = models.ForeignKey(Properties, models.CASCADE, db_column='PropertiesId',blank=True,null=True)  # Field name made lowercase.
    roomtitle = models.TextField(db_column='RoomTitle', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'Rooms'
class Furnitures(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive', blank=True, null=True,default=True)  # Field name made lowercase.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # Field name made lowercase.
    roomtypesid = models.ForeignKey('Roomtypes', models.CASCADE, db_column='RoomTypesId')  # Field name made lowercase.
    furniture = models.TextField(db_column='Furniture', blank=True, null=True)  # Field name made lowercase.
    is_default = models.BooleanField(db_column='IsDefault',blank=True ,null=True)
    user_id=models.ForeignKey(settings.AUTH_USER_MODEL ,db_column='userId',on_delete= models.CASCADE,blank=True,null=True)

    class Meta:
        # managed = False
        db_table = 'Furnitures'


class Furnituresinrooms(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
      # Field name made lowercase.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # Field name made lowercase.
    furnituresid = models.ForeignKey(Furnitures, models.CASCADE, db_column='FurnituresId',blank=True ,null=True)  # Field name made lowercase.
    roomsid = models.ForeignKey('Rooms', models.CASCADE, db_column='RoomsId',blank=True ,null=True)  # Field name made lowercase.
    count=models.IntegerField(db_column='Count',blank=True,null=True)
    quantity = models.IntegerField(db_column='Quantity')  # Field name made lowercase.
    comment=models.TextField(db_column="Comment",blank=True ,null=True)

    class Meta:
        # managed = False
        db_table = 'FurnituresInRooms'


class Furnituresinroomspictures(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
      # Field name made lowercase.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # Field name made lowercase.
    furnituresinroomsid = models.ForeignKey(Furnituresinrooms, models.CASCADE, db_column='FurnituresInRoomsId')  # Field name made lowercase.
    url = models.ImageField(db_column='URL', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'FurnituresInRoomsPictures'

