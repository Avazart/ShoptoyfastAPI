from typing import Annotated

from fastapi import APIRouter, Depends

from src.common.users.check_auth import RoleChecker
from src.database.models.user import User, UserRole

router = APIRouter()


@router.get("/admin")
async def admin_route(
    current_user: Annotated[User, Depends(RoleChecker(UserRole.CLIENT))],
):
    return {"message": "Admin route"}
