from rest_framework import serializers

from products.domain.services import ProductsService


class ProductSerializer(serializers.Serializer):
    owner = serializers.CharField(read_only=True)
    title = serializers.CharField(required=True)
    description = serializers.CharField(required=False, allow_blank=True)