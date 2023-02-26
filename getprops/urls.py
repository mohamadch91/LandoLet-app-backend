from django.urls import path
from .views import *


urlpatterns = [
    path('propsview/', PropsView.as_view(), name='get_prop'),
    path('propertydetail/', PropertyDetail.as_view(), name='get_prop_detail'),
    path('send_to_tenant/', SendtoTenantView.as_view(), name='get_prop_detail'),
    path('generatePDF/<int:id>/', GeneratePDF.as_view(), name='get_prop_pdf'),
    
    

]