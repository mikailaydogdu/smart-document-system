from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from documents.views import home, file_detail, filex,demo

urlpatterns = [
    path('', home, name='home'),
    path('file/', filex, name='file'),
    path('detail/', file_detail, name='detail'),
    path('demo/', demo, name='demo'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
