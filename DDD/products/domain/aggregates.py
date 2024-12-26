from .entities import ProductsEntity
from products.db.repositories import ProductsRepository

class ProductAgregate:

    def __init__(self, product_entity: ProductsEntity):

        self.product_entity = product_entity

    @staticmethod
    def create_product(product_entity: ProductsEntity):

        return ProductAgregate(product_entity)

    @staticmethod
    def get_product_list():

        return ProductAgregate(product_entity)

    @staticmethod
    def get_product_by_id(product_entity: ProductsEntity):

        return ProductAgregate(product_entity)

    @staticmethod
    def update_product(product_entity: ProductsEntity):

        return ProductAgregate(product_entity)

    @staticmethod
    def delete_product(product_entity: ProductsEntity):

        return ProductAgregate(product_entity)