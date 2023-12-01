from pydantic import BaseModel


class UsersHealthValidator(BaseModel):
    user_id: int
    weight: float
    height: float
    gender: str
    pulse: int


class EditHealthRecordValidator(BaseModel):
    user_id: int
    edit_data: str
    new_data: str
