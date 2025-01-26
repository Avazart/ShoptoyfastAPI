from typing import Annotated

import jwt
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jwt import InvalidTokenError
from passlib.context import CryptContext
from starlette import status

from ..settings import Settings, load_settings
from .models import User, UserRole
from .repositories import UserCRUD
from .schemas import TokenData

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


async def authenticate_user(
    username: str, password: str, user_crud: UserCRUD = Depends(UserCRUD)
):
    user = await user_crud.get_user_by_name(username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


async def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    settings: Settings = Depends(load_settings),
    user_crud: UserCRUD = Depends(UserCRUD),
):
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        if username := payload.get("sub"):
            token_data = TokenData(username=username)
            user = user_crud.get_user_by_name(username=token_data.username)
            if user:
                return user
    except InvalidTokenError:
        pass

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )


async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)],
) -> User:
    if current_user.role == UserRole.NOT_ACTIVATED:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
