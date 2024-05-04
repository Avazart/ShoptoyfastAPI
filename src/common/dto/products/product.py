from typing import List, Annotated

from _decimal import Decimal
from pydantic import BaseModel, condecimal, Field

from src.common.constant.constant import BASE_IMAGE_URL
from src.common.dto.base import BaseInDB
from src.common.dto.image.images import ImageInDB, ImageDTO
from src.services.database.models.products.images import Image
from src.services.database.models.products.product import Product

PriceType = Annotated[Decimal, Field(strict=True, max_digits=10, decimal_places=2)]


class ProductCreateDTO(BaseModel):
    name: str
    category_id: int
    price: PriceType
    available: bool = True
    description: str

    class Config:
        from_attributes = True


class ProductInDB(BaseInDB, ProductCreateDTO):
    image_links: list[dict] = []

    class Config:
        from_attributes = True

    @classmethod
    def from_product(cls, product_with_images: Product):
        product_in_db = cls.model_validate(product_with_images)
        product_in_db.image_links = [
            {
                "id": image.id,
                "link": f'{BASE_IMAGE_URL}{image.id}',
                "main": image.is_main_image,
            }
            for image in product_with_images.images
        ]
        return product_in_db
