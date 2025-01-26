from sqlalchemy import select

from ..base_repository import BaseCrud
from .models import User


class UserCRUD(BaseCrud):
    async def get_user_by_name(self, username: str) -> User | None:
        stmt = select(User).where(User.username == username)
        result = await self.session.execute(stmt)
        return result.scalar()
