from typing import Optional, List, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from app.week4.item.model import Item
    from app.week4.memo.model import Memo

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str = Field(unique=True, index=True)

    items: List["Item"] = Relationship(back_populates="owner")
    memos: List["Memo"] = Relationship(back_populates="owner")