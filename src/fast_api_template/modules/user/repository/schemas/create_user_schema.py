from pydantic import BaseModel, EmailStr


class CreateUserSchema(BaseModel):
    email: EmailStr
    hashed_password: str
