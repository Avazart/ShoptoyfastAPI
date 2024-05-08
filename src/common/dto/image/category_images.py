from typing import Optional

from src.common.dto.base import BaseInDB
from pydantic import BaseModel


class CategoryImagesDTO(BaseModel):
    is_main_image: bool

    class Config:
        from_attributes = True


class CategoryImagesInDB(BaseInDB, CategoryImagesDTO):
    category_id: int
    file_id: str

    class Config:
        from_attributes = True
