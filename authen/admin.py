from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from authen.models import User
# Register your models here.

@admin.register(User)
class CustomUserAdmin(BaseUserAdmin):
    model = User
    list_display = ('email', 'id', 'is_active', 'created_at','role','first_name','last_name','postal_code','full_address','phone_no')
    list_filter = ('email', 'id', 'first_name','last_name','postal_code','full_address','phone_no','role')
    fieldsets = (
        ('infos', {'fields': ('email', 'password', 'postal_code', 'first_name', 'last_name', 'phone_no')}),
        ('Permissions', {
         'fields': ('is_staff', 'is_active', 'user_permissions')}),
    )
    
    search_fields = ('email','id','first_name','last_name','postal_code','full_address','phone_no','role')
    ordering = ('email','id','first_name','last_name','postal_code','full_address','phone_no','role')
      
