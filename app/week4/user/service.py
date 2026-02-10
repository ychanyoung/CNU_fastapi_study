from sqlmodel import Session, select
from .model import User


def create_user(session: Session, user: User):
    session.add(instance=user)
    session.commit()
    session.refresh(user)
    return user


def get_users(session: Session):
    return session.exec(select(User)).all()

def get_user_by_id(session: Session, user_id: int):
    return session.get(User, user_id)