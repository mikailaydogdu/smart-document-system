from django.urls import path
# from accounts.views import  UserUpdateView, UserDetailView
#
from .views import RegisterView, ProfileDetailView, UserUpdateView

urlpatterns = [
    path('register/', RegisterView.as_view(), name="signup"),
    path('profile/', UserUpdateView.as_view(), name="update_profile"),
    path('detail/me/', ProfileDetailView.as_view(is_me=True), name="me"),
    path('detail/<int:pk>/', ProfileDetailView.as_view(), name="user_detail"),
]
