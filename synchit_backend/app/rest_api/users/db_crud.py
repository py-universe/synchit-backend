from sqlalchemy.orm import Session
from .models import UserProfile


def create_user_profile(db: Session, user_id: str):
    db_user = UserProfile(user_id=user_id)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return 