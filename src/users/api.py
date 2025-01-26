from typing import Annotated

from fastapi import APIRouter, Depends

from .check_auth import RoleChecker
from .models import User, UserRole

router = APIRouter(prefix="/users", tags=["User"])


@router.get("/admin")
async def admin_route(
    current_user: Annotated[User, Depends(RoleChecker(UserRole.CLIENT))],
):
    return {"message": "Admin route"}
