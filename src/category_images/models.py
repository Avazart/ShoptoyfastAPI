from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from ..base_model import Base


class CategoryImage(Base):
    __tablename__: str = "category_images"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    file_id: Mapped[str]
    category_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("categories.id", ondelete="CASCADE", onupdate="CASCADE"),
    )
    is_main_image: Mapped[bool]
