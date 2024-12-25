from pydantic import BaseModel

class Id(BaseModel):

    id: int = None

    def __str__(self):

        return self.id

class Owner(BaseModel):

    owner: any

    class Config:
            arbitrary_types_allowed = True

    def __str__(self):

        return self.owner

class Title(BaseModel):

    title: str

    def __str__(self):

        return self.title

class Description(BaseModel):

    description: str

    def __str__(self):

        return self.description