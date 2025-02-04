from pydantic import BaseModel

from src.common.dto.base import BaseInDB


class ProductImagesDTO(BaseModel):
    is_main_image: bool


class ProductImagesInDB(BaseInDB, ProductImagesDTO):
    product_id: int
    file_id: str
