from pydantic import BaseModel
from .value_objects import Title, Description, Owner

class ProductsEntity(BaseModel):

    owner: Owner
    title: Title
    description: Description

    class Config:
        orm_mode = True
        from_attributes = True