from products.db.repositories import ProductsRepository
from .entities import ProductsEntity
from .aggregates import ProductAgregate
from .value_objects import Owner, Title, Description

class ProductsService:

    @staticmethod
    def create_product(owner: int, title: str, description: str):

        product_entity = ProductsEntity(
                            owner=Owner(owner=ProductsRepository.get_user_by_id(owner)),
                            title=Title(title=title),
                            description=Description(description=description))
        product_aggregate = ProductAgregate.create_product(product_entity)

        return ProductsRepository.create_product(product_aggregate.product_entity)