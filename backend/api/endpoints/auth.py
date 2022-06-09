from typing import Any

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

import dto
from api import deps

import service

router = InferringRouter()


@cbv(router)
class AuthController:
    db: Session = Depends(deps.get_db)

    @router.post("/login", response_model=dto.Token)
    def login(
            self,
            form_data: OAuth2PasswordRequestForm = Depends()
    ) -> Any:
        token = service.auth_service.authenticate(self.db, form_data.username, form_data.password)

        return {
            "access_token": token,
            "token_type": "bearer",
        }

    @router.post("/register", response_model=dto.User)
    def register(
            self,
            user_to_create: dto.UserCreate,
    ) -> Any:
        try:
            created_user = service.auth_service.create_user(self.db, user_to_create)
        except IntegrityError:
            raise HTTPException(status_code=409, detail="username not unique")
        return created_user
