from sqlalchemy import Integer, VARCHAR, String
from sqlalchemy.orm import Mapped, mapped_column

from app.api.services.databases.models.base import Base


class Category(Base):
    __tablename__ = 'category'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(VARCHAR(255), unique=True, index=True)