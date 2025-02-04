from pydantic import BaseModel

from src.common.dto.base import BaseInDB


class CategoryImagesDTO(BaseModel):
    is_main_image: bool



class CategoryImagesInDB(BaseInDB, CategoryImagesDTO):
    category_id: int
    file_id: str

