from django.contrib import admin
from documents.models import Documents, MyCodes,DocumentDetails

# Register your models here.


admin.site.register(Documents)
admin.site.register(DocumentDetails)
admin.site.register(MyCodes)

