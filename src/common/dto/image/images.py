from typing import Optional

from src.common.dto.base import BaseInDB
from pydantic import BaseModel


class ImageDTO(BaseModel):
    category_id: Optional[int] = None
    product_id: Optional[int] = None
    is_main_image: bool = True

    class Config:
        from_attributes = True


class ImageInDB(ImageDTO, BaseInDB):
    url: str

    class Config:
        from_attributes = True


class ProductCategoryImageDTO(BaseModel):
    is_main_image: bool = True

    class Config:
        from_attributes = True


class ImageIdDTO(BaseModel):
    url: str

    class Config:
        from_attributes = True
