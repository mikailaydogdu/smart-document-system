from django.urls import path, include

from documents.views import index

urlpatterns = [
    path('', index, name='anasayfa'),
]
