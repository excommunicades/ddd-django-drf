from pydantic import BaseModel

from .value_objects import Id, Title, Description, Owner


class ProductEntity(BaseModel):

    id: Id = None
    owner: Owner
    title: Title
    description: Description

    class Config:
        from_attributes = True

    def update(self, title: str = None, description: str = None):
        if title:
            self.title = Title(title=title)
        if description:
            self.description = Description(description=description)