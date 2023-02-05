from django.urls import path
from .views import *


urlpatterns = [
    path('propT_add/', RegisterPropertyTypeView.as_view(), name='Property_type_add'),
    path('propT',PropertyTypeView.as_view(), name='Property_type'),
    path('prop_add/', RegisterPropertyView.as_view(), name='Property_add'),
    path('prop',PropertyView.as_view(), name='Property'),
    path('key_add/', RegisterKeysView.as_view(), name='Keys_add'),
    path('key/', KeyView.as_view(), name='Keys'),
    path('prop_key_add/',RegisterPropertyKeysView.as_view(), name='Property_key_add'),
    path('prop_key/',PropertyKeysView.as_view(), name='Property_key'),
    path('meterT_add/', RegisterMeterTypesView.as_view(), name='Meter_type_add'),
    path('meterT/',MeterTypeView.as_view(), name='Meter_type'),
    path('meter_add/', RegisterMeterReadingView.as_view(), name='Meter_add'),
    path('meter/',MeterReadingView.as_view(), name='Meter'),
]