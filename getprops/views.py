from django.shortcuts import render
from props.serializers import *
from props.models import *
from rooms.serializers import *
from rooms.models import *
import io 
import os
# Create your views here.
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from authen.models import User
from django.shortcuts import get_object_or_404
from django.http import FileResponse
from reportlab.pdfgen import canvas
from django.conf import settings
from pathlib import Path
class PropsView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Properties.objects.all()
    def get(self, request, format=None):
        type=request.query_params.get('type')
        if (type=="tenant"):
            props=Properties.objects.filter(userstenantid=request.user.id)
        else:
            props=Properties.objects.filter(usersownerid=request.user.id)
        res=[]
        all_rooms=Rooms.objects.all()
        room_types=Roomtypes.objects.all()
        for e in props.iterator():
            rooms=all_rooms.filter(propertiesid=e.id)
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
                    'propertytype':propertytype.data,
                }
            }
            res.append(ans)
             


        return Response(data=res,status=status.HTTP_200_OK)

class PropertyDetail(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Properties.objects.all()
    def get(self, request, format=None):
        prop_id=request.query_params.get('p_id',None)
        if(prop_id==None):
              return Response({"message":"need property id query param"},status=status.HTTP_400_BAD_REQUEST)

        prop=get_object_or_404(Properties,id=prop_id)
        
        ser=propertySerilizer(prop,many=False)
        if(ser.data["usersownerid"]!=request.user.id and ser.data["userstenantid"]!=request.user.id):
            return Response({
    "message": "you are not allowed to see this property"
},status=status.HTTP_403_FORBIDDEN)
        meter_reading=Meterreading.objects.all().filter(propertiesid=prop_id)
        property_key=Propertykeys.objects.all().filter(propertiesid=prop_id)
        queryset=Meterstypes.objects.all().filter(user_id=request.user)
        q1=Meterstypes.objects.all().filter(is_default=True)
        meter_type=q1|queryset
        keys=Keys.objects.all()
        meters=[]
        for e in meter_reading.iterator():
            meter=MeterreadingSerializer(e,many=False)
            type=meter_type.filter(id=e.meterstypesid.id)
            mtype=MeterTypeSerializer(type,many=True)
            ans={
                "meter":meter.data,
                "metertype":mtype.data
            }
            meters.append(ans)
        prop_keys=[]    
        for e in property_key.iterator():
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
        for room in rooms.iterator():
            rtype=room_types.filter(id=room.roomtypesid.id)
            rs=RoomTypesSerializer(rtype,many=True)
            pictures=room_pictures.filter(roomsid=room.id)
            room_pictures=RoomPictureSerializer(pictures,many=True)
            fur_in_rooms=fur_in_room.filter(roomsid=room.id)
            fur_in_room_ans=[]
            for fs in fur_in_rooms:
                fur_in_room_picture=fur_in_room_pictures.filter(furnituresinroomsid=fs.id)
                pictures=FurnituresInRoomsPictureSerializer(fur_in_room_picture,many=True)
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
                "pictures":room_pictures.data,
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

class SendtoTenantView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request, format=None):
        full_name=request.data["full_name"]
        signature=request.data["signature"]
        if(full_name==None or signature==None):
            return Response({"message":"need full name and signature in request"},status=status.HTTP_400_BAD_REQUEST)
        if('p_id' not in request.data):
              return Response({"message":"need property id in request"},status=status.HTTP_400_BAD_REQUEST)
        prop_id=request.data["p_id"]
        
        prop=get_object_or_404(Properties,id=prop_id)
        
        if( prop.usersownerid.id!=request.user.id):
            return Response({
    "message": "you are not owner of this property"
},status=status.HTTP_403_FORBIDDEN)
        if('t_email' not in request.data):
              return Response({"message":"need tenant id in request"},status=status.HTTP_400_BAD_REQUEST)    
        tenant_id=request.data["t_email"]
        tenant=get_object_or_404(User,email=tenant_id)
        
        prop.userstenantid=tenant
        prop.landlord_signature=signature
        prop.landlord_signature_name=full_name
        prop.status = 1
        prop.save()
        return Response({
    "message": "property sent to tenant"
},status=status.HTTP_200_OK)
class SendtoOwner(APIView):
    permission_classes = (IsAuthenticated,)
    def post (self,request):
        full_name=request.data["full_name"]
        signature=request.data["signature"]
        if(full_name==None or signature==None):
            return Response({"message":"need full name and signature in request"},status=status.HTTP_400_BAD_REQUEST)
        if('p_id' not  in request.data):
              return Response({"message":"need property id in request"},status=status.HTTP_400_BAD_REQUEST)
        prop_id=request.data["p_id"]
        prop=get_object_or_404(Properties,id=prop_id)
        
        if( prop.userstenantid.id!=request.user.id):
            return Response({
    "message": "you are not tenant  of this property"
},status=status.HTTP_403_FORBIDDEN)        
        prop.tenant_signature=signature
        prop.tenant_signature_name=full_name
        prop.status = 2
        prop.save()
        return Response({
    "message": "property sent back to owner"
},status=status.HTTP_200_OK)

        



class GeneratePDF(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, **kwargs):
        prop_id=int(kwargs['id'])
        prop=get_object_or_404(Properties,id=prop_id)
        ser=propertySerilizer(prop,many=False)
        if(ser.data["usersownerid"]!=request.user.id and ser.data["userstenantid"]!=request.user.id):
            return Response({
    "message": "you are not allowed to see this property"
},status=status.HTTP_403_FORBIDDEN)
        meter_reading=Meterreading.objects.all().filter(propertiesid=prop_id)
        property_key=Propertykeys.objects.all().filter(propertiesid=prop_id)
        queryset=Meterstypes.objects.all().filter(user_id=request.user)
        q1=Meterstypes.objects.all().filter(is_default=True)
        meter_type=q1|queryset
        keys=Keys.objects.all()
        meters=[]
        for e in meter_reading.iterator():
            meter=MeterreadingSerializer(e,many=False)
            type=meter_type.filter(id=e.meterstypesid.id)
            mtype=MeterTypeSerializer(type,many=True)
            ans={
                "meter":meter.data,
                "metertype":mtype.data
            }
            meters.append(ans)
        prop_keys=[]    
        for e in property_key.iterator():
            prop_key=propertyKeysSerializer(e,many=False)
            p_key=keys.filter(id=e.keysid.id)
            key=keySerilizer(p_key,many=True)
            
            ans={
                "propertykey":prop_key.data,
                "key":key.data
            }
            prop_keys.append(ans)    
        rooms=Rooms.objects.filter(propertiesid=prop_id)
        room_types=Roomtypes.objects.all()
        room_pictures=Roompictures.objects.all()
        fur_in_room=Furnituresinrooms.objects.all()
        queryset=Furnitures.objects.all().filter(user_id=request.user)
        q1=Furnitures.objects.all().filter(is_default=True)
        fur=q1|queryset

        fur_in_room_pictures=Furnituresinroomspictures.objects.all()
        room_ans=[]
        for room in rooms.iterator():
            rtype=room_types.filter(id=room.roomtypesid.id)
            rs=RoomTypesSerializer(rtype,many=True)
            pictures=room_pictures.filter(roomsid=room.id)
            room_pictures=RoomPictureSerializer(pictures,many=True)
            fur_in_rooms=fur_in_room.filter(roomsid=room.id)
            fur_in_room_ans=[]
            for fs in fur_in_rooms:
                fur_in_room_picture=fur_in_room_pictures.filter(furnituresinroomsid=fs.id)
                pictures=FurnituresInRoomsPictureSerializer(fur_in_room_picture,many=True)
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
                "pictures":room_pictures.data,
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
        
        buffer = io.BytesIO()
        x = canvas.Canvas(buffer)
        # propert details
        page_counter=1
        x.drawString(300,40,str(page_counter))
        x.drawString(10,800, "owner: "+prop.usersownerid.email)
        if (prop.userslandlordid):
            x.drawString(10,780, "landlord: "+prop.userslandlordid.email)
        if (prop.userstenantid):
            x.drawString(10,760, "tenant: "+prop.userstenantid.email)
        x.drawString(10,740, "address: "+prop.fulladdress)
        x.drawString(10,720, "postal code: "+prop.postalcode)
        # rooms details
        rooms=final_ans["property"]["rooms"]
        x.setFontSize(18)
        
        x.drawString(10,690, "Rooms: ")
        x.setFontSize(12)
        y=680
        for i in range(len(rooms)):
            x.drawString(10,y-10,"-"*400)
            x.drawString(10,y-20, "Room Title: "+rooms[i]["room"]["roomtitle"])
            x.drawString(250,y-20, "Room Type: "+rooms[i]["roomtype"][0]["types"])
            pictures=rooms[i]["pictures"]
            xx=10
            for j in range(len(pictures)):
                pic_path=Path(str(settings.BASE_DIR)+pictures[j]["image"])
                x.drawImage(pic_path, xx, y-130, width=100, height=100)
                str_width=x.stringWidth(pictures[j]["comment"])
                counter=0
                if (str_width>150):
                    while(str_width>150):
                        if(counter>5):
                            x.drawString(xx,y-150-counter*10, ".....")
                            break
                        else:
                            x.drawString(xx,y-150-counter*10, pictures[j]["comment"][counter*15:(counter+1)*15])
                            counter+=1
                            str_width-=150
                else:
                    x.drawString(xx,y-150, pictures[j]["comment"])
                if (j%3==2):
                    y=y-200
                    if (y<0):
                        x.showPage()
                        page_counter+=1
                        x.drawString(300,40,str(page_counter))
                        y=780
                    xx=10
                else:
                    xx+=200
            x.showPage()
            page_counter+=1
            x.drawString(300,40,str(page_counter))
            xx=10
            y=780
            furniture=rooms[i]["furnituresinrooms"]
            x.setFontSize(18)
            
            x.drawString(10,y, "Furniture: ")
            x.setFontSize(12)
            
            for j in range(len(furniture)):
                x.drawString(10,y-10,"-"*400)
                fur=furniture[j]["furniture"]
                type=furniture[j]["furnituretype"][0]
                x.drawString(10,y-20, "Furniture Type: "+type["furniture"])
                x.drawString(250,y-20, "Furniture quantity: "+str(fur["quantity"]))
                if (fur["comment"]):
                    str_width=x.stringWidth(fur["comment"])
                    counter=0
                    if (str_width>450):
                        while(str_width>450):
                            if(counter>5):
                                x.drawString(10,y-40-counter*10, ".....")
                                break
                            else:
                                x.drawString(10,y-40-counter*10, fur["comment"][counter*80:(counter+1)*80])
                                counter+=1
                                str_width-=450
                    else:
                        x.drawString(10,y-40, fur["comment"])
                furniture_pictures=furniture[j]["pictures"]
                xx=10
                
                if (counter!=0):
                    y=y-50-counter*10
                else:
                    y-=50
                for k in range(len(furniture_pictures)):
                    pic_path=Path(str(settings.BASE_DIR)+furniture_pictures[k]["image"])
                    x.drawImage(pic_path, xx, y-100, width=100, height=100)
                    if (k%3==2):
                        y=y-200
                    if (y<0):
                        x.showPage()
                        page_counter+=1
                        x.drawString(300,40,str(page_counter))
                        
                        y=780
                        xx=10
                    else:
                        xx+=200
                    if (k==len(furniture_pictures)-1):
                        y-=110   
                y-=40
                if(y<0):
                    x.showPage()
                    page_counter+=1
                    x.drawString(300,40,str(page_counter))
                    y=780
                    
            x.showPage()
            page_counter+=1
            x.drawString(300,40,str(page_counter))
            meters=final_ans["property"]["meters"]
            xx=10
            y=780
            x.setFontSize(18)
            x.drawString(10,y, "Meters: ")
            x.setFontSize(12)
            
            for i in range(len(meters)):
                x.drawString(10,y-10,"-"*400)
                x.drawString(10,y-20, "Meter Type: "+meters[i]["metertype"][0]["meters"])
                x.drawString(250,y-20, "Meter Value: "+str(meters[i]["meter"]["metervalue"]))
                if (meters[i]["meter"]["pictureurl"]):
                    pic_path=Path(str(settings.BASE_DIR)+meters[i]["meter"]["pictureurl"])
                    x.drawImage(pic_path, xx, y-130, width=100, height=100)
                    y-=130
                    continue
                y-=50
                if(y<0):
                    x.showPage()
                    page_counter+=1
                    x.drawString(300,40,str(page_counter))
            if(len(meters)>5):
                x.showPage()
                page_counter+=1
                x.drawString(300,40,str(page_counter))
                xx=10
                y=780
            keys=final_ans["property"]["propertykeys"]
            y-=50
            x.setFontSize(18)
            x.drawString(10,y, "keys: ")
            x.setFontSize(12)
            for i in range(len(keys)):
                x.drawString(10,y-10,"-"*400)
                x.drawString(10,y-20, "key  Type: "+keys[i]["key"][0]["types"])
                x.drawString(250,y-20, "Key count: "+str(keys[i]["propertykey"]["count"]))
                y-=50    
                if(y<0):
                    x.showPage()
                    page_counter+=1
                    x.drawString(300,40,str(page_counter))
                
                
            
            
        
        x.showPage()
        page_counter+=1
        x.drawString(300,40,str(page_counter))
        x.setFontSize(18)
        x.drawString(10,800, "Signatures : ")
        x.setFontSize(12)
        # draw furnitures 
        x.drawString(60,780, "landlord : "+prop.landlord_signature_name)
        x.drawString(370,780, "tenant : "+prop.tenant_signature_name)
        x.drawImage(os.path.join(settings.BASE_DIR,'/media/props/signatures/',prop.landlord_signature.path), 40, 620, width=150, height=150)
        x.drawImage(os.path.join(settings.BASE_DIR,'/media/props/signatures/',prop.landlord_signature.path), 340, 620, width=150, height=150)      
        # x.drawImage(str(settings.BASE_DIR)+'images.jpg', 250, 730, width=100, height=100)
        x.save()
        buffer.seek(0)
        return FileResponse(buffer, as_attachment=True, filename='test.pdf')

