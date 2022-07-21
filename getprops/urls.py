from django.urls import path
from .views import *


urlpatterns = [
    path('propsview/', propsview.as_view(), name='get_prop'),
    path('propertydetail/', propertydetail.as_view(), name='get_prop_detail'),
]