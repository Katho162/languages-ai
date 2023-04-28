from fastapi import APIRouter, HTTPException, Path
from fastapi import Depends, Body
from fastapi.encoders import jsonable_encoder
import math
from ..config.engine import SessionLocal
from sqlalchemy.orm import Session

from ..auth.schema import LoginInputSchema, LoginOutputSchema
from ..users.schema import CreateUser
from ..users.crud import create_user
from ..auth.bearer import JWTBearer
from ..auth.handler import signJWT
from ..users.model import User

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter(
    prefix="/auth",
    tags=['Authentification'],
    responses={
        404: { "error": "Not found." }
    }
)

@router.post("/login")
async def login(redirect_to : str, data: LoginInputSchema = Body(...), db: Session = Depends(get_db)):

    _user = db.query(User).filter(User.username == data.username).first()

    if not _user.verify_password(data.pwd, _user.pwd):
        raise HTTPException(status_code=403, detail="Invalid credentials.")
    
    return signJWT(jsonable_encoder(_user))

@router.post('/register')
async def register(user: CreateUser = Body(...), db : Session = Depends(get_db)):
    _user = jsonable_encoder(await create_user(db, user))
    return signJWT(_user)
