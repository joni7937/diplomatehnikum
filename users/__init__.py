from pydantic import BaseModel


class LoginUserValidator(BaseModel):
    email: str
    password: str


class RegisterUserValidator(BaseModel):
    username: str
    email: str
    phone_number: str
    password: str


class EditUserValidator(BaseModel):
    id: int
    edit_data: str
    new_data: str


