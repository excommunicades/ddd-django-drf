from pydantic import BaseModel, EmailStr, constr

class Email(BaseModel):

    email: EmailStr

    def __str__(self):

        return self.email

class Password(BaseModel):

    password: constr(min_length=8)

    def __str__(self):

        return self.password
