from typing import Optional
from fastapi import APIRouter, FastAPI, HTTPException
from pydantic import BaseModel

items_router = APIRouter(prefix="/items", tags=["items"])


class Item(BaseModel):
    id: int
    data: str
    price: int

items: list[Item] = [
    Item(id=1, data='apple', price=4000),
    Item(id=2, data='banana', price=7000),
    Item(id=3, data='cherry', price=500),
    ]

class ItemCreate(BaseModel):
    data: str
    price: int

class ItemDelete(BaseModel):
    item_id: int

class ItemPut(BaseModel):
    data: str
    price: int

class ItemPatch(BaseModel):
    data: Optional[str] = None
    price: Optional[int] = None



@items_router.post("/")
async def create_item(payload: ItemCreate):
    item: tuple[Item] = Item(id=len(items)+1, **payload.model_dump())
    items.append(item)
    return item


@items_router.get("/{item_id}")
async def read_item(item_id: int):
    for i in items:
        if item_id == i.id:
            return {"result": i}
    raise HTTPException(status_code=404, detail='Item not found')
    


@items_router.get("/all/")
async def all_items():
    return get_items()


def find_itemByPrice(q: int):
    temp: list[str] = []
    for i in items:
        if q >= i.price:
            temp.append(i.data)
    if not temp: return {"result": "not found"}
    return {"can buy" :temp}

def find_itemByName(q: str):
    for i in items:
        if q==i.data:
            return {"result": i}
    return {"result": "not found"}

def get_items():
    return {"all items": items}

@items_router.delete("/{item_id}")
def remove_item(item_id: int):
    for i in items:
        if i.id == item_id:
            items.remove(i)
            return {"result": i['data']}
    raise HTTPException(status_code=404, detail='Item not found')

@items_router.get("")
async def _find(q: str | None = None):
    if q is None: return get_items()
    if q.isdigit():
        return find_itemByPrice(int(q))
    elif isinstance(q, str):
        return find_itemByName(q)
    return {"result": "not valid parameter"}

#같은 path(/items)일 경우 --> 현재는 /items/all/ 로 바꿔놨음
# def ~~(q: str | None : None):
#      if q is str: 함수 호출
#      else 함수 호출
#이런식으로 구현할 수도 있음


#put / patch
#put : 하나를 전체 다 바꾼다
#patch : 하나의 일부를 바꾼다

@items_router.put("/{item_id}")
def update_item(payload: ItemPut, item_id: int):
    for i in items:
        if i.id == item_id:
            i.data = payload.data
            i.price = payload.price
            return {"result": i}
    raise HTTPException(status_code=404, detail='Item not found')

@items_router.patch("/{item_id}")
def patch_item(payload: ItemPatch, item_id: int):
    for i in items:
        if i.id == item_id:
            if payload.data is not None:
                i.data = payload.data
            if payload.price is not None:
                 i.price = payload.price
            return {"result": i}
    raise HTTPException(status_code=404, detail='Item not found')