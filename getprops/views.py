from django.shortcuts import render
from props.serializers import *
from props.models import *
from rooms.serializers import *
from rooms.models import *

# Create your views here.
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
class propsview(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Properties.objects.all()
    def get(self, request, format=None):
        res=[]
        props=Properties.objects.all()
        props=props.filter(usersownerid=request.user.id)
        all_rooms=Rooms.objects.all()
        room_types=Roomtypes.objects.all()
        status=PropertyStatus.objects.all()
        for e in props:
            rooms=all_rooms.filter(propertiesid=e.id)
            stat=status.filter(property_id=e.id)
            stat=PropertyStatusSerilizer(stat,many=True)
            proptype=Propertytypes.objects.all().filter(id=e.propertytypesid.id)
            propertytype = propertyTypeSerializer(proptype,many=True)
            rooms = RoomSerializer(rooms,many=True)

            room_ans=[]
            for room in rooms.data:
                rtype=room_types.filter(id=room['roomtypesid'])
                rs=RoomTypesSerializer(rtype,many=True)
                ans={
                    "room":room,
                    "roomtype":rs.data
                }  
                room_ans.append(ans)
            property= propertySerilizer(e,many=False)
            ans={
                "property":{
                    "data":property.data,
                    "rooms":room_ans,
                    "status":stat.data,
                    'propertytype':propertytype.data,
                }
            }
            res.append(ans)
             


        return Response(data=res,status=status.HTTP_204_NO_CONTENT)

class propertydetail(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Properties.objects.all()
    def get(self, request, format=None):
        prop_id=request.query_params.get('p_id')
        prop=self.queryset.filter(id=prop_id)
        if(prop_id==None):
              return Response("need property id query param",status=status.HTTP_400_BAD_REQUEST)
        if(len(prop)==0):
            return Response("invalid property id",status=status.HTTP_404_NOT_FOUND)
        ser=propertySerilizer(prop,many=True)
        if(ser.data[0]["usersownerid"]!=request.user.id):
            return Response("this user cannot acces property",status=status.HTTP_403_FORBIDDEN)
        meter_reading=Meterreading.objects.all().filter(propertiesid=prop_id)
        property_key=Propertykeys.objects.all().filter(propertiesid=prop_id)
        queryset=Meterstypes.objects.all().filter(user_id=request.user)
        q1=Meterstypes.objects.all().filter(is_default=True)
        meter_type=q1|queryset
        keys=Keys.objects.all()
        meters=[]
        for e in meter_reading:
            meter=MeterreadingSerializer(e,many=False)
            type=meter_type.filter(id=e.meterstypesid.id)
            mtype=MeterTypeSerializer(type,many=True)
            ans={
                "meter":meter.data,
                "metertype":mtype.data
            }
            meters.append(ans)
        prop_keys=[]    
        for e in property_key:
            prop_key=propertyKeysSerializer(e,many=False)
            p_key=keys.filter(id=e.keysid.id)
            key=keySerilizer(p_key,many=True)
            
            ans={
                "propertykey":prop_key.data,
                "key":key.data
            }
            prop_keys.append(ans)    
        rooms=Rooms.objects.all().filter(propertiesid=prop_id)
        room_types=Roomtypes.objects.all()
        room_pictures=Roompictures.objects.all()
        fur_in_room=Furnituresinrooms.objects.all()
        queryset=Furnitures.objects.all().filter(user_id=request.user)
        q1=Furnitures.objects.all().filter(is_default=True)
        fur=q1|queryset

        fur_in_room_pictures=Furnituresinroomspictures.objects.all()
        room_ans=[]
        for room in rooms:
            rtype=room_types.filter(id=room.roomtypesid.id)
            rs=RoomTypesSerializer(rtype,many=True)
            pictures=room_pictures.filter(roomsid=room.id)
            pictures=RoomPictureSerializer(pictures,many=True)
            fur_in_rooms=fur_in_room.filter(roomsid=room.id)
            fur_in_room_ans=[]
            for fs in fur_in_rooms:
                fur_in_room_pictures=fur_in_room_pictures.filter(furnituresinroomsid=fs.id)
                pictures=FurnituresInRoomsPictureSerializer(fur_in_room_pictures,many=True)
                ftype=fur.filter(id=fs.furnituresid.id)
                ftype=FurnituresSerializer(ftype,many=True)
                furniture=FurnituresInRoomsSerializer(fs,many=False)
                temp_ans={
                    "furniture":furniture.data,
                    "pictures":pictures.data,
                    "furnituretype":ftype.data
                }
                fur_in_room_ans.append(temp_ans)
            roomser=RoomSerializer(room,many=False)    
            ans={
                "room":roomser.data,
                "roomtype":rs.data,
                "pictures":pictures.data,
                "furnituresinrooms":fur_in_room_ans
            }
            room_ans.append(ans)
        final_ans={
                "property":{
                    "data":ser.data,
                    "rooms":room_ans,
                    "meters":meters,
                    "propertykeys":prop_keys,

                }
        }
        return Response(data=final_ans,status=status.HTTP_200_OK)    

