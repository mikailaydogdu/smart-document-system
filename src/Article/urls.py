from django.urls import path

from Article.views import *  #article_update, article_add, ArticleListView, revizyon_list, ArticleAdd

urlpatterns = [
    path('', ArticleListView.as_view(), name='home'),
    # path('revizyondetail/<int:pk>', revizyon_list, name='revizyonlist'),
    path('revizyondetail/<int:pk>', ArticleItemListView.as_view(), name='revizyonlist'),
    # path('detail/<int:pk>/    ', ArticleDetailView.as_view(), name='article-detail'),
    # path('ekle/', article_add, name='article_add'),
    path('ekleclass/', ArticleCreate.as_view(), name='article_add'),
    # path('guncelle/', article_update, name='article_update'),
    path('guncelle/', ArticileItemCreate.as_view(), name='article_update'),
]