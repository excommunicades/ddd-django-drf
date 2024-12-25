from rest_framework import serializers

from products.domain.services import ProductsService

class ProductSerializer(serializers.Serializer):

    owner = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    description = serializers.CharField()

    def create(self, validated_data):

        user = self.context['request'].user

        product_entity = ProductsService.create_product(
            owner=int(user.id),
            title=validated_data['title'],
            description=validated_data['description'],
        )

        return product_entity
