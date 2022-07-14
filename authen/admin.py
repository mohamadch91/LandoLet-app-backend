from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from authen.models import User,Userinrole,Roles
# Register your models here.

class CustomUserAdmin(BaseUserAdmin):
    model = User
    list_display = ('username', 'is_staff', 'is_active', 'is_superuser')
    list_filter = ('username', 'is_staff', 'is_active',)
    fieldsets = (
        ('اطلاعات اصلی', {'fields': ('username', 'password', 'postalcode', 'firstname', 'lastname', 'phoneno')}),
        ('Permissions', {
         'fields': ('is_staff', 'is_active', 'user_permissions')}),
    )
    
    search_fields = ('is_staff',)
    ordering = ('username',)
admin.site.register(User,CustomUserAdmin)        
admin.site.register(Userinrole)
admin.site.register(Roles)
