from typing import List

from django.contrib.auth.models import User

from products.db.model import Products
from products.domain.entities import ProductEntity
from products.domain.value_objects import Id, Owner, Title, Description
class ProductsRepository:

    @staticmethod
    def create_product(product_entity: ProductEntity) -> ProductEntity:

        product = Products.objects.create(
            owner=product_entity.owner.owner,
            title=product_entity.title.title,
            description=product_entity.description.description,
        )

        return ProductEntity(
            owner=Owner(owner=product.owner),
            title=Title(title=product.title),
            description=Description(description=product.description),)

    @staticmethod
    def get_product_list() -> List[ProductEntity]:

        product_list = Products.objects.all()

        return [
            ProductEntity(
                id=Id(id=product_entity.id),
                owner=Owner(owner=product_entity.owner),
                title=Title(title=product_entity.title),
                description=Description(description=product_entity.description)
            )
            for product_entity in product_list
        ]

    @staticmethod
    def get_product_by_id(id: int) -> ProductEntity:

        try:
            product_entity = Products.objects.get(id=id)

        except Exception as e:
            raise ValueError(str(e))

        return product_entity

    @staticmethod
    def update_product(product_entity: ProductEntity) -> ProductEntity:

        try:
            product = Products.objects.get(id=int(product_entity.id.id))

            if product.owner != product_entity.owner.owner:
                raise ValueError("You must to be an owner of this product for update operation.")

        except Exception as e:
            raise ValueError(str(e))

        product.title = product_entity.title.title

        if product_entity.description.description:
            product.description = product_entity.description.description

        product.save()

        return product

    @staticmethod
    def delete_product(id: int, request_user_id: int) -> ProductEntity:

        try:
            product_entity = Products.objects.get(id=id)

            if product_entity.owner.id != request_user_id:
                raise ValueError("You must to be an owner of this product for update operation.")

            product_entity.delete()

        except Exception as e:
            raise ValueError(str(e))

        return product_entity
