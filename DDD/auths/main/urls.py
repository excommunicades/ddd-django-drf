from django.urls import path


from api.views.auth_views import (
    RegisterUser,
    LoginUser,
)
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('register', RegisterUser.as_view(), name='register_user'),
    path('login', LoginUser.as_view(), name='login_user'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]