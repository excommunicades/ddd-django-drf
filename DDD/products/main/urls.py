from django.urls import path
from api.views.products_views import (
    CreateProduct,
)

urlpatterns = [
    path('create', CreateProduct.as_view(), name='create_product')
]
