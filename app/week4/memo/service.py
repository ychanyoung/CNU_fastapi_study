from sqlmodel import Session, select
from .model import Memo


def create_memo(session: Session, memo: Memo):
    session.add(instance=memo)
    session.commit()
    session.refresh(memo)
    return memo


def get_memos(session: Session):
    return session.exec(select(Memo)).all()

def delete_memo(session: Session, memo_id: int):
    memo = session.get(Memo, memo_id)
    if memo:
        session.delete(memo)
        session.commit()
        return True
    return False