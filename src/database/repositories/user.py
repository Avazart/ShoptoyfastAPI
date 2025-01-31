from sqlalchemy import select

from src.database.models.user import User
from src.database.repositories import BaseCrud


class UserCRUD(BaseCrud):
    async def get_user_by_name(self, username: str) -> User | None:
        stmt = select(User).where(User.username == username)
        result = await self.session.execute(stmt)
        return result.scalar()
