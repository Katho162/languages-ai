from .model import User
from .schema import CreateUser, UpdateUser, UserSchema
from sqlalchemy.orm import Session


async def get_users(db: Session, page: int = 1, limit: int = 100):
    return db.query(User).offset(((page - 1) * limit)).limit(limit).all()

async def get_users_by_id(db: Session, user_id: str):
    return db.query(User).filter(User.id == user_id).first()

async def create_user(db: Session, user: CreateUser):
    _user = User(
        username=user.username,
        pwd=user.pwd,
        fullname=user.fullname,
        birthdate=user.birthdate
    )
    db.add(_user)
    db.commit()
    db.refresh(_user)
    return _user


async def remove_user(db: Session, user_id: str):
    _user = await get_users_by_id(db=db, user_id=user_id)
    db.delete(_user)
    return db.commit()


async def update_user(db: Session, user_id: str, data: UpdateUser):
    _user = get_users_by_id(db=db, user_id=user_id)

    _user.username = data.username
    _user.pwd = data.pwd
    _user.fullname = data.fullname
    _user.birthdate = data.birthdate

    db.commit()
    db.refresh(_user)
    return _user