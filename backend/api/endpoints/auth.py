from datetime import timedelta
from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from starlette import status

import repo, domain, dto
from api import deps
from core import security
from core.config import settings

router = APIRouter()


@router.post("/login", response_model=dto.Token)
def login(
        db: Session = Depends(deps.get_db), form_data: OAuth2PasswordRequestForm = Depends()
) -> Any:
    user = repo.user_repo.authenticate(
        db, username=form_data.username, password=form_data.password
    )
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return {
        "access_token": security.create_access_token(
            user.id, expires_delta=access_token_expires
        ),
        "token_type": "bearer",
    }


@router.post("/login/test-token", response_model=dto.User)
def test_token(current_user: domain.User = Depends(deps.get_current_user)) -> Any:
    """
    Test access token
    """
    return current_user


@router.post("/register", response_model=dto.User)
def register(user_to_create: dto.UserCreate, db: Session = Depends(deps.get_db)) -> Any:
    try:
        created_user = repo.user_repo.create(db, user_in=user_to_create)
    except IntegrityError:
        raise HTTPException(status_code=409, detail="username not unique")
    return created_user
