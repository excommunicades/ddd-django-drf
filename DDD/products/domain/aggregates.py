from .entities import ProductEntity
from products.db.repositories import ProductsRepository

#TODO: Add some business logic, business rule

class ProductAggregate:

    def __init__(self, product_entity: ProductEntity):

        self.product_entity = product_entity

    @staticmethod
    def create_product(product_entity: ProductEntity):

        return ProductAggregate(product_entity)

    @staticmethod
    def get_product_list():

        return ProductAggregate(product_entity)

    @staticmethod
    def get_product_by_id(product_entity: ProductEntity):

        return ProductAggregate(product_entity)

    @staticmethod
    def update_product(product_entity: ProductEntity):

        return ProductAggregate(product_entity)

    @staticmethod
    def delete_product(product_entity: ProductEntity):

        return ProductAggregate(product_entity)