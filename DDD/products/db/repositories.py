from django.contrib.auth.models import User

from products.db.model import Products
from products.domain.entities import ProductsEntity
from products.domain.value_objects import Owner, Title, Description
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