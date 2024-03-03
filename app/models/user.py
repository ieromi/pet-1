from pydantic import BaseModel
from datetime import date
from typing import Union


class User(BaseModel):
    id: int
    first_name: str
    patronymic: Union[str, None] = None
    last_name: Union[str, None] = None
    dob: Union[date, None] = None
    tel_num: str
    email: Union[str, None] = None


external_data = {
    "id": "123",
    "first_name": "Анастасия",
    "tel_num": "+7988888888"
}


user = User(**external_data)

print(user)