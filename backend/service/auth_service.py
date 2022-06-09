from datetime import timedelta

from fastapi import HTTPException
from sqlalchemy.orm import Session

import dto
import repo
from core import security
from core.config import settings
from core.security import verify_password, get_password_hashed
from domain import User


class AuthService:
    def authenticate(self, db: Session, username: str, password: str):
        user = repo.user_repo.get_by_username(
            db, username=username
        )

        if not user or not verify_password(password, user.hashed_password):
            raise HTTPException(status_code=400, detail="Incorrect username or password")

        access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)

        return security.create_access_token(
            user.id, expires_delta=access_token_expires
        )

    def create_user(self, db: Session, user_in: dto.UserCreate):
        db_user = User(
            username=user_in.username,
            hashed_password=get_password_hashed(user_in.password),
            fullname=user_in.fullname,
        )
        return repo.user_repo.create(db, user=db_user)


auth_service = AuthService()
