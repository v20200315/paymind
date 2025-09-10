from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home_page"),
    path("login", views.login, name="login_page"),
    path("register", views.register, name="register_page"),
    path("forgot-password", views.forgot_password, name="forgot_password_page"),
    path("dashboard", views.dashboard, name="dashboard_page"),
    path("settings/profile", views.profile, name="profile_page"),
    path("settings/security", views.security, name="security_page"),
    path("sandbox/user", views.sandbox_user, name="sandbox_user_page"),
    path("sandbox/member", views.sandbox_member, name="sandbox_member_page"),
    path("sandbox/admin", views.sandbox_admin, name="sandbox_admin_page"),
    path("sandbox/owner", views.sandbox_owner, name="sandbox_owner_page"),
]
