from django.contrib import admin

from main_api.models import User, Role

# Register your models here.
@admin.register (User)
class UserAdmin (admin.ModelAdmin):
    list_display = ['id', 'username', 'password']


@admin.register (Role)
class RoleAdmin (admin.ModelAdmin):
    list_display = ['id', 'rolename']