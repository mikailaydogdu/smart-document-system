from django.contrib import admin
from documents.models import Documents, Documents_user, MyCodes

# Register your models here.


admin.site.register(Documents)
admin.site.register(Documents_user)
admin.site.register(MyCodes)

