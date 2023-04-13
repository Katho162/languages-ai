from typing import Optional, List
from pydantic import BaseModel

class UserSchema(BaseModel):
    id: str
    username: str
    pwd: str
    fullname: str
    birthdate: str
    created_at: str 
    updated_at: str

class PaginatedUser(BaseModel):
    data: List[UserSchema] | None
    page: int
    total_pages: int
    total: int

class CreateUser(BaseModel):
    username: str
    pwd: str
    fullname: str
    birthdate: str

class UpdateUser(BaseModel):
    username : Optional[str]
    pwd: Optional[str]
    fullname: Optional[str]
    birthdate: Optional[str]