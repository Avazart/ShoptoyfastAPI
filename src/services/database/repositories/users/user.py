from sqlalchemy import insert, select

from src.common.dto.users.user import UserDTO, UserInDB
from src.services.database.models.users.user import User
from src.services.database.repositories import BaseCrud


class UserCRUD(BaseCrud):
    async def get_user_by_name(self, username: str) -> User | None:
        stmt = select(User).where(User.username == username)
        result = await self.session.execute(stmt)
        return result.scalar()
