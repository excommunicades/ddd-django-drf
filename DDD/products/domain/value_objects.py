from pydantic import BaseModel, Field

class Id(BaseModel):

    id: int = Field(...)

    def __str__(self):

        return str(self.id)

class Owner(BaseModel):

    '''Owner of product | Owner of update/delete request'''

    owner: any

    class Config:
        arbitrary_types_allowed = True

    def __str__(self):
        return str(self.owner)

class Title(BaseModel):

    title: str

    def __str__(self):

        return self.title

class Description(BaseModel):

    description: str | None = None

    def __str__(self):

        return self.description