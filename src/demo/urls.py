from django.urls import path
from .views import *

urlpatterns = [
    path('add', FileUploadView.as_view()),
    path('', index, name='index'),
    path('x', exm, name='index'),
]