from django.urls import path

from documents.views import home, fileuploads, image


urlpatterns = [
    path('', home, name='home'),
    path('file/', fileuploads, name='upload files'),
    path('images/', image, name='upload files'),

]
