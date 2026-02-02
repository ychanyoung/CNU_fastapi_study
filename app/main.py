from typing import Optional
from fastapi import APIRouter, FastAPI, HTTPException
from pydantic import BaseModel

from app.week3.items_router import items_router
from app.week3.memo_router import memo_router
# from app.week2.practice1 import router as practice1_router
# from app.week2.practice2 import router as practice2_router
# from app.week2.practice3 import router as practice3_router

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


# app.include_router(practice1_router)
# app.include_router(practice2_router)
# app.include_router(practice3_router)
app.include_router(items_router)
app.include_router(memo_router)