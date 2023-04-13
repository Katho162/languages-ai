from fastapi import FastAPI
from .routers import users
from .config.engine import engine, Base
# Import models

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get('/', tags=['Hello world!'])
async def index():
    return {"message": "Hello world! This is the User's Authentification Service!"}


app.include_router(users.router)

