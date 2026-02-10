from typing import Optional
from fastapi import APIRouter, FastAPI, HTTPException
from pydantic import BaseModel
from contextlib import asynccontextmanager
from app.db import create_db_and_tables
from app.week4.item.router import router as item_router
from app.week4.user.router import router as user_router
from app.week4.memo.router import router as memo_router

from app.week3.items_router import items_router
#from app.week3.memo_router import memo_router
# from app.week2.practice1 import router as practice1_router
# from app.week2.practice2 import router as practice2_router
# from app.week2.practice3 import router as practice3_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}


# app.include_router(practice1_router)
# app.include_router(practice2_router)
# app.include_router(practice3_router)
# app.include_router(items_router)
# app.include_router(memo_router)

app.include_router(router=item_router)
app.include_router(router=user_router)
app.include_router(router=memo_router)