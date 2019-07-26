from django.contrib import admin
from documents.models import Documents, DocumentDetails

@admin.register(Documents)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['label', 'type', 'active']
    list_display_links = ['label', 'type']
    search_fields = ['label', 'type']
    list_filter = ["created_date"]

    class Meta:
        model = Documents


@admin.register(DocumentDetails)
class DocumentDetailAdmin(admin.ModelAdmin):
    list_display = ['document', 'user', 'create_date', 'file', 'file_sha1']
    list_display_links = ['document', 'create_date']
    search_fields = ['document', 'user']
    list_filter = ["create_date"]

    class Meta:
        model = DocumentDetails
