from typing import Optional

from src.common.dto.base import BaseInDB
from pydantic import BaseModel


class ProductImagesDTO(BaseModel):
    is_main_image: bool

    class Config:
        from_attributes = True


class ProductImagesInDB(BaseInDB, ProductImagesDTO):
    product_id: int
    file_id: str

    class Config:
        from_attributes = True
