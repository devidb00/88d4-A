from typing import Optional
from pydantic import BaseModel, Field

class AccountSchema(BaseModel):
    name: str     = Field()
    email: str    = Field()
    password: str = Field()

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Tarik ID BELLOUCH",
                "email": "tarikidb.dev@gmail.com",
                "password": "123654"
            }
        }