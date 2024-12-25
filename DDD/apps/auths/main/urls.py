from django.urls import path


from apps.api.views.auth_views import RegisterUser
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('register', RegisterUser.as_view(), name='register_user'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]