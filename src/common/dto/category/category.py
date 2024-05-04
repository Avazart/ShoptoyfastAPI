from datetime import datetime

from pydantic import BaseModel

from src.common.dto.base import BaseInDB


class CategoryCreateDTO(BaseModel):
    name: str

    class Config:
        from_attributes = True


class CategoryInDB(CategoryCreateDTO, BaseInDB):
    id: int

    class Config:
        from_attributes = True
