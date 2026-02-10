from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.db import get_session
from .model import Item
from .service import create_item, delete_item, get_items

router = APIRouter(prefix="/items", tags=["items"])

@router.post("/", response_model=Item)
def create(item: Item, session: Session = Depends(get_session)):
    return create_item(session, item)

@router.get("/", response_model=list[Item])
def list_all(session: Session = Depends(get_session)):
    return get_items(session)

@router.delete("/{item_id}")
def delete(item_id: int, session: Session = Depends(get_session)):
    success = delete_item(session, item_id)
    if not success:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Successfully deleted"}