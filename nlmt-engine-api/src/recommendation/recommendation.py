from fastapi import APIRouter
from pydantic import BaseModel
from typing import List
 
# importing
from ..model.model import predict_pipeline

router = APIRouter()

class LanguageModel(BaseModel):
    name: str

class LanguageOut:
    language: str
    corr: float

class LanguageIn(BaseModel):
    userId: str
    languages: List[LanguageModel]

@router.post("/")
async def recommend(data: LanguageIn, response_model=LanguageOut):

    print(predict_pipeline(data.languages[0].name))

    return data