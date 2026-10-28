from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import Register_View


urlpatterns = [
    # Register
    path("register/", Register_View.as_view(), name="register"),

    # Login -> access + refresh token
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),

    # Refresh access token
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]