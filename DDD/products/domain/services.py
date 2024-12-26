from products.db.repositories import ProductsRepository
from .entities import ProductsEntity
from .aggregates import ProductAgregate
from .value_objects import Id, Owner, Title, Description

class ProductsService:

    @staticmethod
    def create_product(owner: any, title: str, description: str):

        product_entity = ProductsEntity(
                            owner=Owner(owner=owner),
                            title=Title(title=title),
                            description=Description(description=description))

        product_aggregate = ProductAgregate.create_product(product_entity)

        return ProductsRepository.create_product(product_aggregate.product_entity)

    @staticmethod
    def get_product_list():

        products = ProductsRepository.get_product_list()

        return [
            {
                'id': product.id.id,
                'owner': str(product.owner.owner),
                'title': str(product.title.title),
                'description': str(product.description.description)
            }
            for product in products
        ]

    @staticmethod
    def get_product_by_id(id: int):

        product_entity = ProductsRepository.get_product_by_id(id)
        product_aggregate = ProductAgregate.get_product_by_id(product_entity)

        return {
            'id': product_aggregate.product_entity.id,
            'owner': product_aggregate.product_entity.owner.username,
            'title': product_aggregate.product_entity.title,
            'description': product_aggregate.product_entity.description
        }

    @staticmethod
    def udpate_product(id: int, owner:any,  title: str, description: str | None):

        product_entity = ProductsEntity(
                            id=Id(id=id),
                            owner=Owner(owner=owner),
                            title=Title(title=title),
                            description=Description(description=description))

        product_aggregate = ProductAgregate.update_product(product_entity)

        return ProductsRepository.update_product(product_aggregate.product_entity)

    @staticmethod
    def delete_product(id: int, request_user_id: int):

        return ProductsRepository.delete_product(id, request_user_id)