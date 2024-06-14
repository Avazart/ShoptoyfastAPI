
from pydantic import BaseModel

from src.common.dto.base import BaseInDB


class ProductImagesDTO(BaseModel):
    is_main_image: bool

    class Config:
        from_attributes = True


class ProductImagesInDB(BaseInDB, ProductImagesDTO):
    product_id: int
    file_id: str

    class Config:
        from_attributes = True
