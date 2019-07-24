from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from accounts.models import CustomUser


@admin.register(CustomUser)
class UserTable(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields',
         {'fields': ('birth_date', 'telephone', 'image', 'follow')}
         ),
    )
