from typing import Optional
from fastapi import APIRouter, FastAPI, HTTPException
from pydantic import BaseModel

memo_router = APIRouter(prefix="/memo", tags=["memo"])


class Memo(BaseModel):
    id: int
    title: str
    content: str

memos: list[Memo] = [
    Memo(id=1, title='week', content="asdad"),
    Memo(id=2, title='2_01', content="dadasd"),
    Memo(id=3, title='2_02', content="CNU study"),
    ]

class MemoCreate(BaseModel):
    title: str
    content: str

class MemoDelete(BaseModel):
    memo_id: int

class MemoPut(BaseModel):
    title: str
    content: str

class MemoPatch(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None


#index
@memo_router.get("/")
async def read_item():
    return {"all of memos" : memos}


#post
#1. append
@memo_router.post("/")
async def create_memo(payload: MemoCreate):
    memo: tuple[Memo] = Memo(id=memos[-1].id+1, **payload.model_dump())
    memos.append(memo)
    return memo

#get
@memo_router.get("/{memo_id}")
async def findMemoById(memo_id: int):
    for m in memos:
        if m.id == memo_id:
            return m
    raise HTTPException(status_code=404, detail='Memo not found')

#put
@memo_router.put("/{memo_id}")
async def update_memo(payload: MemoPut, memo_id: int):
    for m in memos:
        if m.id == memo_id:
            m.title = payload.title
            m.content = payload.content
            return m
    raise HTTPException(status_code=404, detail='Memo not found')

#patch
@memo_router.patch("/{memo_id}")
async def fix_memo(payload: MemoPatch, memo_id: int):
    for m in memos:
        if m.id == memo_id:
            if payload.title is not None:
                m.title = payload.title
            if payload.content is not None:
                m.content = payload.content
            return m
    raise HTTPException(status_code=404, detail='Memo not found')

#delete
@memo_router.delete("/{item_id}")
def remove_item(item_id: int):
    for m in memos:
        if m.id == item_id:
            memos.remove(m)
            return {"remove": m}
    raise HTTPException(status_code=404, detail='Item not found')