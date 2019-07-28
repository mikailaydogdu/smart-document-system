from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="base/anasayfa.html"), name="anasayfa"),
    path('logged_out/', TemplateView.as_view(template_name="registration/logged_out.html"), name="logged_out"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page="logged_out"), name="logout"),
    # path('documenet', include('documents.urls')),
    path('accounts/', include('accounts.urls')),
    path('article/', include('Article.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
