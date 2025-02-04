from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..base_model import Base


class Category(Base):
    __tablename__: str = "categories"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True, index=True)

    products = relationship("Product", backref="categories")
    images = relationship("CategoryImage", backref="categories")

    # parent_id: Mapped[int] = mapped_column(
    #     Integer, ForeignKey("categories.id"), nullable=True
    # )
    #
    # parent: Mapped["Category"] = relationship(
    #     "Category", backref="children", remote_side=[id]
    # )
    # children: Mapped[list["Category"]] = relationship(
    #     "Category", backref="parent", remote_side=[parent_id]
    # )
