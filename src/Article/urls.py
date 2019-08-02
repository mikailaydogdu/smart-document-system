from django.conf import settings
from django.urls import path, re_path
from django.views.static import serve

from Article.views import *


urlpatterns = [
    path('', ArticleListView.as_view(), name='home'),
    path('ekleclass/', ArticleCreateView.as_view(), name='article_add'),
    path('search/', ArticleSearchView.as_view(), name='search'),
    path('detail/<int:pk>', ArticleDetailView.as_view(), name='detail'),

    path('revizyondetail/<int:pk>/', ArticleItemListView.as_view(), name='revizyonlist'),
    path('revizyondetail/<int:pk>/ekle/', ArticileItemCreate.as_view(), name='article_item_add'),
]

if settings.DEBUG:
    urlpatterns.append(re_path(r'^media/(?P<path>.*)$',
                               serve,
                               {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}))
