from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="users/login.html"),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(), name="logout",),
    path("singup/", views.SignUpView.as_view(), name="signup"),
    path("profile/", views.ProfileUpdateView.as_view(), name="profile"),
    path("profile/connect", views.ProfileConnectView.as_view(), name="profile_connect"),
    path(
        "profile/disconnect",
        views.ProfileDisconnectView.as_view(),
        name="profile_disconnect",
    ),
]
