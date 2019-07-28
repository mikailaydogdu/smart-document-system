from django.urls import path

from Article.views import home, article_update, article_add

urlpatterns = [
    path('', home, name='articlehome'),
    path('ekle/', article_add, name='article_add'),
    path('guncelle/', article_update, name='article_update'),
]