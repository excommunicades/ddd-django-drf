from rest_framework import serializers

from products.domain.services import ProductsService

class ProductSerializer(serializers.Serializer):

    owner = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True)
    description = serializers.CharField(required=False)
