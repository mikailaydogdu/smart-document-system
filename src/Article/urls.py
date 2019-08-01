from django.urls import path

from Article.views import *  #article_update, article_add, ArticleListView, revizyon_list, ArticleAdd

urlpatterns = [
    path('', ArticleListView.as_view(), name='home'),
    path('revizyondetail/<int:pk>/', ArticleItemListView.as_view(), name='revizyonlist'),
    path('ekleclass/', ArticleCreateView.as_view(), name='article_add'),
    path('guncelle/', ArticileItemCreate.as_view(), name='article_update'),

    path('revizyondetail/<int:pk>/ekle/', ArticileItemCreate.as_view(), name='article_item_add'),
    # path('revizyondetail/<int:pk>/add/', ItemCreate.as_view(), name='revizyonekle'),
]