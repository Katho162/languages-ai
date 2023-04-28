from typing import Optional, List
from pydantic import BaseModel
from ..users.schema import UserSchema, CreateUser

class LoginInputSchema(BaseModel):
    username: str
    pwd: str

class LoginOutputSchema(BaseModel):
    data: UserSchema
    token: str
    valid_until: str
