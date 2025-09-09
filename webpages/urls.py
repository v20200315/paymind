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
    path("samples/user", views.samples_user, name="samples_user_page"),
    path("samples/member", views.samples_member, name="samples_member_page"),
    path("samples/admin", views.samples_admin, name="samples_admin_page"),
    path("samples/owner", views.samples_owner, name="samples_owner_page"),
]
