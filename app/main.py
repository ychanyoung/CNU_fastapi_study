from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.week2.practice1 import router as practice1_router
from app.week2.practice2 import router as practice2_router
from app.week2.practice3 import router as practice3_router

app = FastAPI()

items: list[dict] = [
    {'id':1, 'data':'apple', 'price': 4000}, 
    {'id':2, 'data':'banana', 'price': 7000}, 
    {'id':3, 'data':'cherry', 'price': 500}, 
    ]

class ItemCreate(BaseModel):
    data: str
    price: int

@app.post("/items")
async def create_item(payload: ItemCreate):
    item: dict[str, int] = {'id': len(items)+1, **payload.model_dump()}
    items.append(item)
    return item

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    for i in items:
        if item_id == i.get('id'):
            return {"result": i}
    raise HTTPException(status_code=404, detail='Item not found')
    


@app.get("/items/all/")
async def all_items():
    return get_items()


def find_itemByPrice(q: int):
    temp: list[str] = []
    for i in items:
        if q >= i.get('price'):
            temp.append(i.get('data'))
    if not temp: return {"result": "not found"}
    return {"can buy" :temp}

def find_itemByName(q: str):
    for i in items:
        if q==i.get('data'):
            return {"result": i}
    return {"result": "not found"}

def get_items():
    return {"all items": items}

@app.get("/items")
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



app.include_router(practice1_router)
app.include_router(practice2_router)
app.include_router(practice3_router)