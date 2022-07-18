from django.urls import path
from .views import *


urlpatterns = [
    path('roomP_add/', registerRoomPictureview.as_view(), name='Room picture add'),
    path('roomP',RoomPictureView.as_view(), name='Room picture'),

    path('roomT_add/', registerRoomTypesView.as_view(), name='Room type add'),
    path('roomT',RoomTypesView.as_view(), name='Room type'),


    path('room_add/', registerRoomsView.as_view(), name='Room add'),
    path('room/', RooomView.as_view(), name='Room'),
    
    path('furtniture_add/',registerFurnitureView.as_view(), name='Furniture add'),
    path('furniture/',Furnitureview.as_view(), name='Furniture'),

    path('finroom_add/', registerFurnitureInRoomView.as_view(), name='Furniture in room add'),
    path('finroom/',FurnitureInRoomView.as_view(), name='Furniture in room'),

    path('finroomP_add/', registerFurnituresinroomspicturesView.as_view(), name='Furniture in room Picture add'),
    path('finroomP/',FurnitureinroomspicturesView.as_view(), name='Furniture in room Picture '),
]