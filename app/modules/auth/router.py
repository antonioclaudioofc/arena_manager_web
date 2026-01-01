from fastapi import APIRouter, Depends
from typing import Annotated
from fastapi.security import OAuth2PasswordRequestForm
from app.dependencies import db_dependency
from app.schemas.auth import AuthCreate
from app.schemas.token import Token
from starlette import status
from app.modules.auth.service import AuthService

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)


@router.post("/", status_code=status.HTTP_201_CREATED)
def register(
    db: db_dependency,
    user_request: AuthCreate
):
    AuthService.register(user_request, db)


@router.post("/token", response_model=Token)
def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: db_dependency
):
    return AuthService.login(form_data, db)
