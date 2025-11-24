from fastapi import APIRouter, Depends
from core.config import ALGORITHM, SECRET_KEY
from dependencies import db_dependency
from schemas.auth import AuthCreate
from schemas.token import Token
from models.auth import Users
from starlette import status
from core.security import hash_password
from datetime import datetime, timedelta, timezone
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from core.security import bcrypt_context
from jose import jwt

router = APIRouter()


def autheticate_user(username: str, password: str, db):
    user = db.query(Users).filter(Users.username == username).first()
    if not user:
        return False
    if not bcrypt_context.verify(password, user.hashed_password):
        return False
    return user


def create_access_token(username: str, user_id: int, expires_delta: timedelta):
    encode = {"sub": username, "id": user_id}
    expires = datetime.now(timezone.utc) + expires_delta
    encode["exp"] = expires
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)


@router.post("/auth", status_code=status.HTTP_201_CREATED)
async def create_user(db: db_dependency, user_request: AuthCreate):
    auth_model = Users(
        email=user_request.email,
        username=user_request.username,
        first_name=user_request.first_name,
        hashed_password=hash_password(user_request.password),
        role=user_request.role,
        created_at=datetime.now(timezone.utc)
    )

    db.add(auth_model)
    db.commit()


@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: db_dependency):
    user = autheticate_user(form_data.username, form_data.password, db)
    if not user:
        return "Failed Authentication"

    token = create_access_token(user.username, user.id, timedelta(minutes=20))

    return {"access_token": token, "token_type": "bearer"}
