from django.urls import path
from api.views.products_views import (
    ProductAPIView,
)

urlpatterns = [
    path('create', ProductAPIView.as_view(), name='create_product'),
    path('all', ProductAPIView.as_view(), name='get_product_list'),
    path('<int:product_id>', ProductAPIView.as_view(), name='get_product'),
]
