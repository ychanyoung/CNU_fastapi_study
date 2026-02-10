from sqlalchemy import Engine
from sqlmodel import SQLModel, create_engine, Session

import app.week4.item.model
import app.week4.user.model
import app.week4.memo.model


engine: Engine = create_engine(url="sqlite:///./app.db", echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(bind=engine)

def get_session():
    with Session(bind=engine) as session:
        yield session