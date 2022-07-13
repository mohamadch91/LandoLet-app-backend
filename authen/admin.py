from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from authen.models import User
# Register your models here.
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('username','phone','email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name','title','birth','address','city','zip')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone','username','email', 'password1', 'password2'),
        }),
    )
    list_display = ('phone','email','username', 'first_name', 'last_name', 'is_staff')
    search_fields = ('phone','email', 'first_name', 'last_name')
    ordering = ('phone',)