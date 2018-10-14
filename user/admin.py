from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as UAdmin
from .models import User


@admin.register(User)
class UserAdmin(UAdmin):
    """Custom User Admin
    """

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {
         'fields': ('first_name', 'last_name', 'email', 'phone_number', 'volunteer')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
                                    'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
