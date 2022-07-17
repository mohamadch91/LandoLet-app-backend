from django.urls import path
from .views import *


urlpatterns = [
    path('propT_add/', registerPropertyTypeview.as_view(), name='Property_type'),
    path('prop_add/', registerPropertyview.as_view(), name='Property'),
    path('key_add/', registerkeysview.as_view(), name='Key'),
    path('prop_key_add',registerPropertyKeysview.as_view(), name='Property_key'),

]