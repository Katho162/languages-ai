from fastapi import FastAPI
from .recommendation import recommendation
import uvicorn

app = FastAPI()

app.include_router(recommendation.router, prefix='/recommendation')

if __name__ == "__main__":
    uvicorn.run(app=app, host='127.0.0.1', port=8001)
