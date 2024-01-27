from django.urls import path
from django.contrib.auth import views

from user.views import UserCreateView, UserDetailView, UserUpdateView

urlpatterns = [
    path("sign-up/", UserCreateView.as_view(), name="sign-up"),
    path("me/", UserDetailView.as_view(), name="me"),
    path("me/update/", UserUpdateView.as_view(), name="update"),
]

app_name = "user"
