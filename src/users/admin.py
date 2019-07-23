from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from users.models import UserTable


@admin.register(UserTable)
class UserTable(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields',
         {'fields' : ('birth_date','telephone', 'image','fallow')}
         ),
    )

