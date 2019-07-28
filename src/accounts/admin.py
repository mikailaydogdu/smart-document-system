from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from accounts.models import CustomUserTable


@admin.register(CustomUserTable)
class UserTable(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields',
         {'fields': ('ident_no','birth_date', 'telephone','mobile_tel', 'image','job','task' )}
         ),
    )
