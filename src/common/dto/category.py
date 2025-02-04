from typing import Any

from pydantic import BaseModel

from src.common.constants.constant import BASE_CATEGORY_IMAGE_URL
from src.common.dto.base import BaseInDB


class CategoryDTO(BaseModel):
    name: str


class CategoryInDB(CategoryDTO, BaseInDB):
    pass


class CategoryWithImagesInDB(CategoryInDB):
    image_links: list[dict]

    @classmethod
    def model_validate(
        cls,
        obj: Any,
        *,
        strict: bool | None = None,
        from_attributes: bool | None = None,
        context: dict[str, Any] | None = None,
    ):
        product_in_db = CategoryInDB.model_validate(
            obj,
            strict=strict,
            from_attributes=from_attributes,
            context=context,
        )
        image_links = [
            {
                "id": image.id,
                "link": f"{BASE_CATEGORY_IMAGE_URL}{image.id}",
                "main": image.is_main_image,
            }
            for image in obj.images
        ]
        return CategoryWithImagesInDB(
            **product_in_db.model_dump(),
            image_links=image_links,
        )
