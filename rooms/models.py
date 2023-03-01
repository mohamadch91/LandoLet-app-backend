from itertools import count
from django.db import models
from props.models import Properties
from django.conf import settings
# Create your models here.


class Roompictures(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)   
       
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)   
    roomsid = models.ForeignKey('Rooms', models.CASCADE, db_column='RoomsId',db_index=True)   
    image = models.ImageField(db_column='URL', blank=True, null=True)   
    comment = models.TextField(db_column='Comment', blank=True, null=True)   
    t_comment=models.TextField(db_column="T_Comment",blank=True ,null=True)
    class Meta:
        # managed = False
        db_table = 'RoomPictures'


class Roomtypes(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)   
       
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)   
    types = models.TextField(db_column='Types', blank=True, null=True)   
    class Meta:
        # managed = False
        db_table = 'RoomTypes'


class Rooms(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)   
       
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)   
    roomtypesid = models.ForeignKey(Roomtypes, models.CASCADE, db_column='RoomTypesId',blank=True,null=True,db_index=True)   
    propertiesid = models.ForeignKey(Properties, models.CASCADE, db_column='PropertiesId',blank=True,null=True,db_index=True)   
    roomtitle = models.TextField(db_column='RoomTitle', blank=True, null=True)   

    class Meta:
        # managed = False
        db_table = 'Rooms'
class Furnitures(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)   
    isactive = models.BooleanField(db_column='IsActive', blank=True, null=True,default=True,db_index=True)   
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)   
    roomtypesid = models.ForeignKey('Roomtypes', models.CASCADE, db_column='RoomTypesId',db_index=True)   
    furniture = models.TextField(db_column='Furniture', blank=True, null=True)   
    is_default = models.BooleanField(db_column='IsDefault',blank=True ,null=True)
    user_id=models.ForeignKey(settings.AUTH_USER_MODEL ,db_column='userId',on_delete= models.CASCADE,blank=True,null=True,db_index=True)

    class Meta:
        # managed = False
        db_table = 'Furnitures'


class Furnituresinrooms(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)   
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)   
    furnituresid = models.ForeignKey(Furnitures, models.CASCADE, db_column='FurnituresId',blank=True ,null=True,db_index=True)   
    roomsid = models.ForeignKey('Rooms', models.CASCADE, db_column='RoomsId',blank=True ,null=True,db_index=True)   
    quantity = models.IntegerField(db_column='Quantity')   
    comment=models.TextField(db_column="Comment",blank=True ,null=True)
    t_comment=models.TextField(db_column="T_Comment",blank=True ,null=True)

    class Meta:
        # managed = False
        db_table = 'FurnituresInRooms'


class Furnituresinroomspictures(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True,db_index=True)   
       
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)   
    furnituresinroomsid = models.ForeignKey(Furnituresinrooms, models.CASCADE, db_column='FurnituresInRoomsId',db_index=True)   
    image = models.ImageField(db_column='URL', blank=True, null=True)   

    class Meta:
        # managed = False
        db_table = 'FurnituresInRoomsPictures'

