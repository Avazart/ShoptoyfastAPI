from sqlalchemy import insert, select, delete

from src.common.dto.image.category_images import (
    CategoryImagesInDB,
    CategoryImagesDTO,
)
from src.services.database.models.products.images import CategoryImage
from src.services.database.repositories import BaseCrud


class CategoryImageCrud(BaseCrud):
    async def create(
        self, file_id: str, category_id: int, new_image: CategoryImagesDTO
    ):
        stmt = (
            insert(CategoryImage)
            .values(
                file_id=file_id, category_id=category_id, **new_image.__dict__
            )
            .returning(CategoryImage)
        )
        result = await self.session.execute(stmt)
        await self.session.commit()
        result_orm = result.scalar_one_or_none()
        return CategoryImagesInDB.model_validate(result_orm)

    async def get_one(self, image_id: int) -> CategoryImagesInDB | None:
        stmt = select(CategoryImage).where(CategoryImage.id == image_id)
        result = await self.session.execute(stmt)
        await self.session.commit()
        result_orm = result.scalar()
        return (
            CategoryImagesInDB.model_validate(result_orm)
            if result_orm
            else None
        )

    async def delete(self, image_id: int) -> CategoryImagesInDB | None:
        stmt = (
            delete(CategoryImage)
            .where(CategoryImage.id == image_id)
            .returning(CategoryImage)
        )
        result = await self.session.execute(stmt)
        await self.session.commit()
        result_orm = result.scalar()
        return (
            CategoryImagesInDB.model_validate(result_orm)
            if result_orm
            else None
        )
