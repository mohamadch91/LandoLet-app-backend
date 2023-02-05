from django.urls import path
from .views import *


urlpatterns = [
    path('roomP_add/',  RegisterRoomPictureView.as_view(), name='Room picture add'),
    path('roomP',RoomPictureView.as_view(), name='Room picture'),

    path('roomT_add/',  RegisterRoomTypesView.as_view(), name='Room type add'),
    path('roomT',RoomTypesView.as_view(), name='Room type'),


    path('room_add/',  RegisterRoomsView.as_view(), name='Room add'),
    path('room/', RooomView.as_view(), name='Room'),
    
    path('furniture_add/', RegisterFurnitureView.as_view(), name='Furniture add'),
    path('furniture/',FurnitureView.as_view(), name='Furniture'),

    path('finroom_add/',  RegisterFurnitureInRoomView.as_view(), name='Furniture in room add'),
    path('finroom/',FurnitureInRoomView.as_view(), name='Furniture in room'),

    path('finroomP_add/',  RegisterFurnituresinroomspicturesView.as_view(), name='Furniture in room Picture add'),
    path('finroomP/',FurnitureinroomspicturesView.as_view(), name='Furniture in room Picture '),
]