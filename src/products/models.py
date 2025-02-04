from sqlalchemy import DECIMAL, Boolean, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..base_model import Base


class Product(Base):
    __tablename__: str = "products"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True, index=True)
    category_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("categories.id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=True,
    )
    price: Mapped[int] = mapped_column(DECIMAL(10, 2), nullable=False)
    available: Mapped[bool] = mapped_column(Boolean, default=True)
    description: Mapped[str] = mapped_column(Text, default=None, nullable=True)
    images = relationship("ProductImage", backref="products")


class CharacteristicName(Base):
    __tablename__: str = "characteristic_names"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True, index=True)


class CharacteristicValue(Base):
    __tablename__: str = "characteristic_values"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    value: Mapped[str]

    characteristic_id: int  # ->  CharacteristicName.id
    product_id: int  # -> Product.id
