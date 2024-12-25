from pydantic import BaseModel, constr
from .value_objects import Password, Email

class UserEntity(BaseModel):

    username: constr(min_length=3, max_length=150)
    email: Email
    password: Password

    class Config:
        from_attributes = True
