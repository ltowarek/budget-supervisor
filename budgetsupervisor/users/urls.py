from django.contrib.auth import views as auth_views
from django.urls import path
from users.tokens import user_tokenizer

from budgetsupervisor import settings

from . import views

urlpatterns = [
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="users/login.html"),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("singup/", views.SignUpView.as_view(), name="signup"),
    path(
        "activate/<str:user_id>/<str:token>/",
        views.UserActivateView.as_view(),
        name="activate",
    ),
    path(
        "reset-password",
        auth_views.PasswordResetView.as_view(
            template_name="users/password_reset_form.html",
            email_template_name="users/password_reset_email.html",
            subject_template_name="users/password_reset_subject.txt",
            success_url=settings.LOGIN_URL,
            token_generator=user_tokenizer,
        ),
        name="password_reset",
    ),
    path(
        "reset-password-confirmation/<str:uidb64>/<str:token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="users/password_reset_confirm.html",
            post_reset_login=True,
            token_generator=user_tokenizer,
            success_url=settings.LOGIN_REDIRECT_URL,
        ),
        name="password_reset_confirm",
    ),
    path("profile/", views.ProfileUpdateView.as_view(), name="profile"),
    path("profile/delete", views.UserDeleteView.as_view(), name="user_delete"),
    path("profile/connect", views.ProfileConnectView.as_view(), name="profile_connect"),
    path(
        "profile/disconnect",
        views.ProfileDisconnectView.as_view(),
        name="profile_disconnect",
    ),
]
