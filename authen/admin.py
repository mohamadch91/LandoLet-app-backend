from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from authen.models import User
# Register your models here.

class CustomUserAdmin(BaseUserAdmin):
    model = User
    list_display = ('username', 'id', 'is_active', 'regdate','role','first_name','last_name','postal_code','full_address','phone_no')
    list_filter = ('username', 'id', 'first_name','last_name','postal_code','full_address','phone_no','role')
    fieldsets = (
        ('infos', {'fields': ('username', 'password', 'postal_code', 'first_name', 'last_name', 'phone_no')}),
        ('Permissions', {
         'fields': ('is_staff', 'is_active', 'user_permissions')}),
    )
    
    search_fields = ('username','id','first_name','last_name','postal_code','full_address','phone_no','role')
    ordering = ('username','id','first_name','last_name','postal_code','full_address','phone_no','role')
admin.site.register(User,CustomUserAdmin)        
