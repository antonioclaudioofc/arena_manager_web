from fastapi import APIRouter, Depends
from dependencies import db_dependency
from typing import Annotated
from modules.auth.service import AuthService
from starlette import status
from schemas.auth import UserVerification
from modules.user.service import UserService


router = APIRouter(
    prefix="/user",
    tags=["user"]
)

user_dependency = Annotated[dict, Depends(AuthService.get_current_user)]


@router.get("/", status_code=status.HTTP_200_OK)
def get_user(
    user: user_dependency,
    db: db_dependency
):
    return UserService.get_profile(user, db)


@router.put("/password", status_code=status.HTTP_204_NO_CONTENT)
def change_password(
    user: user_dependency,
    user_verification: UserVerification,
    db: db_dependency
):
    UserService.change_password(user, user_verification, db)
