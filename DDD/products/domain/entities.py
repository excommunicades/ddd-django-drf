from pydantic import BaseModel
from .value_objects import Id, Title, Description, Owner

class ProductsEntity(BaseModel):

    id: Id = None
    owner: Owner = None
    title: Title = None
    description: Description = None

    class Config:
        from_attributes = True