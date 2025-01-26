from enum import IntEnum

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from ..base_model import Base


class UserRole(IntEnum):
    NOT_ACTIVATED = 0
    CLIENT = 1
    ADMIN = 3


class User(Base):
    __tablename__: str = "user"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String, unique=True)
    email: Mapped[str] = mapped_column(String, unique=True)
    hashed_password: Mapped[str]
    role: Mapped[int]
