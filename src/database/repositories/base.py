from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.session import get_session


class BaseCrud:
    def __init__(self, db: AsyncSession = Depends(get_session)):
        self.session = db
