from typing import Optional

from sqlalchemy import insert, select, delete

from src.common.dto.image.images import (
    ProductCategoryImageDTO,
    ImageInDB,
    ImageDTO,
)
from src.services.database.models.products.images import Image
from src.services.database.repositories import BaseCrud


class ImageCrudCategory(BaseCrud):
    async def create(
            self, url: str, category_id: int, new_image: ProductCategoryImageDTO
    ):
        stmt = (
            insert(Image)
            .values(url=url, category_id=category_id, **new_image.__dict__)
            .returning(Image)
        )
        result = await self.session.execute(stmt)
        await self.session.commit()
        result_orm = result.scalar_one_or_none()
        return ImageInDB.model_validate(result_orm)


class ImageCrudProduct(BaseCrud):
    async def create(
            self, url: str, product_id: int, new_image: ProductCategoryImageDTO
    ):
        stmt = (
            insert(Image)
            .values(url=url, product_id=product_id, **new_image.__dict__)
            .returning(Image)
        )
        result = await self.session.execute(stmt)
        await self.session.commit()
        result_orm = result.scalar_one_or_none()
        return ImageInDB.model_validate(result_orm)


class ImageCrud(BaseCrud):
    async def get_one(self, image_id: int):
        stmt = select(Image).where(Image.id == image_id)
        result = await self.session.execute(stmt)
        await self.session.commit()
        result_orm = result.scalar()
        return ImageInDB.model_validate(result_orm) if result_orm else None

    async def delete(self, image_id: int):
        stmt = delete(Image).where(Image.id == image_id)
        result = await self.session.execute(stmt)
        await self.session.commit()
        result_orm = result.scalar()
        return ImageInDB.model_validate(result_orm) if result_orm else None
