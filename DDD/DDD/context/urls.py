from rest_framework.schemas import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

from django.views.generic import TemplateView
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('apps.auths.main.urls')),
    path('api_schema', get_schema_view(title='Swagger', description='Guide for the REST API'), name='api_schema'),
    path('swagger', TemplateView.as_view(
                        template_name='swagger.html',
                        extra_context={'schema_url':'api_schema'}
                        ), name='swagger-ui'),
]
