from typing import List

from django.contrib.auth.models import User

from products.db.model import Products
from products.domain.entities import ProductsEntity
from products.domain.value_objects import Id, Owner, Title, Description
class ProductsRepository:

    @staticmethod
    def create_product(product_entity: ProductsEntity) -> ProductsEntity:

        product = Products.objects.create(
            owner=product_entity.owner.owner,
            title=product_entity.title.title,
            description=product_entity.description.description,
        )

        return ProductsEntity(
            owner=Owner(owner=product.owner),
            title=Title(title=product.title),
            description=Description(description=product.description),)

    @staticmethod
    def get_user_by_id(id: int) -> ProductsEntity:

        return User.objects.filter(id=id).first()

    @staticmethod
    def get_product_list() -> List[ProductsEntity]:

        product_list = Products.objects.all()

        return [
            ProductsEntity(
                id=Id(id=product_entity.id),
                owner=Owner(owner=product_entity.owner),
                title=Title(title=product_entity.title),
                description=Description(description=product_entity.description)
            )
            for product_entity in product_list
        ]

    @staticmethod
    def get_product_by_id(id: int) -> ProductsEntity:

        try:
            product_entity = Products.objects.get(id=id)

        except Exception as e:
            raise ValueError(str(e))

        return product_entity

    @staticmethod
    def update_product(product_entity: ProductsEntity) -> ProductsEntity:

        try:
            product = Products.objects.get(id=id)

        except Exception as e:
            raise ValueError(str(e))

        product.title = product_entity.title.title
        product.description = product_entity.description.description
        product.save()

        return product