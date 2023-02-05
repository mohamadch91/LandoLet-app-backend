from django.urls import path
from .views import *


urlpatterns = [
    path('propsview/', propsview.as_view(), name='get_prop'),
    path('propertydetail/', propertydetail.as_view(), name='get_prop_detail'),
    path('send_to_tenant/', sendtoTenantView.as_view(), name='get_prop_detail'),
    path('generatePDF/<int:id>/', generatePDF.as_view(), name='get_prop_detail'),
    

]