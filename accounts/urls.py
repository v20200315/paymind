from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from .views import (
    RegisterView,
    JWTLoginView,
    SessionLoginView,
    JWTLogoutView,
    SessionLogoutView,
)

router = DefaultRouter()

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/jwt/", JWTLoginView.as_view(), name="jwt_login"),
    path("login/session/", SessionLoginView.as_view(), name="session_login"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("logout/jwt/", JWTLogoutView.as_view(), name="logout"),
    path("logout/session/", SessionLogoutView.as_view(), name="logout"),
    path("", include(router.urls)),
]
