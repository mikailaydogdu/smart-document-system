from django.contrib import admin
from Article.models import Article, Revisions


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'type', 'active']
    list_display_links = ['title', 'type']
    search_fields = ['title', 'type']
    list_filter = ['title']


    class Meta:
        model = Article

@admin.register(Revisions)
class RevisonsAdmin(admin.ModelAdmin):
    list_display = ['file','file_sha1']