from sqlalchemy import delete, insert, select

from ..base_repository import BaseCrud
from .models import ProductImage
from .schemas import (
    ProductImagesDTO,
    ProductImagesInDB,
)


class ProductImageCrud(BaseCrud):
    async def create(
        self, file_id: str, product_id: int, new_image: ProductImagesDTO
    ) -> ProductImagesInDB:
        stmt = (
            insert(ProductImage)
            .values(
                file_id=file_id, product_id=product_id, **new_image.__dict__
            )
            .returning(ProductImage)
        )
        result = await self.session.execute(stmt)
        await self.session.commit()
        result_orm = result.scalar_one_or_none()
        return ProductImagesInDB.model_validate(result_orm)

    async def get_one(self, image_id: int) -> ProductImagesInDB | None:
        stmt = select(ProductImage).where(ProductImage.id == image_id)
        result = await self.session.execute(stmt)
        await self.session.commit()
        result_orm = result.scalar()
        return (
            ProductImagesInDB.model_validate(result_orm)
            if result_orm
            else None
        )

    async def delete(self, image_id: int) -> ProductImagesInDB | None:
        stmt = (
            delete(ProductImage)
            .where(ProductImage.id == image_id)
            .returning(ProductImage)
        )
        result = await self.session.execute(stmt)
        await self.session.commit()
        result_orm = result.scalar()
        return (
            ProductImagesInDB.model_validate(result_orm)
            if result_orm
            else None
        )
