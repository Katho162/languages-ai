from fastapi import APIRouter, HTTPException, Path
from fastapi import Depends
import math
from ..config.engine import SessionLocal
from sqlalchemy.orm import Session

from ..users.model import User
from ..users.schema import UserSchema, PaginatedUser, CreateUser, UpdateUser
from ..users import crud

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter(
    prefix="/users",
    tags=['Users'],
    responses={
        404: { "error": "Not found." }
    }
)

@router.get("/")
async def get_users(page: int = 1, limit: int = 100, db: Session = Depends(get_db)):
    _users = await crud.get_users(db, page, limit)
    count = db.query(User).count()
    total_pages = math.ceil(count / limit)
    page = max(min(page, 1), total_pages)
    return { "data": _users, "page": page, "total_pages": total_pages, "total": count }

@router.get("/{user_id}")
async def get_user_by_id(user_id: str, db: Session = Depends(get_db)):
    _user = await crud.get_users_by_id(db, user_id)
    return _user

@router.delete("/{user_id}")
async def remove_user(user_id: str, db: Session = Depends(get_db)):
    _user = await crud.remove_user(db, user_id)
    return _user

@router.put("/{user_id}")
async def update_user(user_id: str, data: UpdateUser, db: Session = Depends(get_db)):
    _user = await crud.update_user(db, user_id, data)
    return _user

@router.post('/',  response_model=UserSchema)
async def create_user(data : CreateUser, db: Session = Depends(get_db)):
    await crud.create_user(db, data)
    return []