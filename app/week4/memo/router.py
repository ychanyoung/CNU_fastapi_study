from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.db import get_session
from .model import Memo
from .service import delete_memo, get_memos, create_memo

router = APIRouter(prefix="/memos", tags=["memos"])

@router.post("/", response_model=Memo)
def create(memo: Memo, session: Session = Depends(get_session)):
    return create_memo(session, memo)

@router.get("/", response_model=list[Memo])
def list_all(session: Session = Depends(get_session)):
    return get_memos(session)

@router.delete("/{memo_id}")
def delete(memo_id: int, session: Session = Depends(get_session)):
    success = delete_memo(session, memo_id)
    if not success:
        raise HTTPException(status_code=404, detail="Memo not found")
    return {"message": "Successfully deleted"}