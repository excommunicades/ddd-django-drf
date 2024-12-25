from pydantic import BaseModel
from .value_objects import Id, Title, Description, Owner

class ProductsEntity(BaseModel):

    id: Id = None
    owner: Owner
    title: Title
    description: Description

    class Config:
        from_attributes = True