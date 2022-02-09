from typing import Optional

from sqlalchemy.orm import Session

from core.security import get_password_hashed, verify_password
from domain.user import User
from dto.user import UserCreate


class UserRepo:
    def get_by_username(self, db: Session, *, username: str) -> Optional[User]:
        return db.query(User).filter(User.username == username).first()

    def get(self, db: Session, id: int) -> Optional[User]:
        return db.query(User).filter(User.id == id).first()

    def create(self, db: Session, *, user_in: UserCreate) -> User:
        db_user = User(
            username=user_in.username,
            hashed_password=get_password_hashed(user_in.password),
            fullname=user_in.fullname,
        )

        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    def authenticate(self, db: Session, *, username: str, password: str) -> Optional[User]:
        user = self.get_by_username(db, username=username)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user


user_repo = UserRepo()
