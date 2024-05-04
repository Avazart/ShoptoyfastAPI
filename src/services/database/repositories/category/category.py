from typing import Optional, List

from sqlalchemy import insert, select, update, delete
from sqlalchemy.engine import row

from src.common.dto.category.category import CategoryCreateDTO, CategoryInDB

from src.services.database.repositories.base import BaseCrud

from src.services.database.models.products.category import Category


class CategoryCrud(BaseCrud):
    async def create(self, new_category: CategoryCreateDTO):
        stmt = (
            insert(Category)
            .values(**new_category.__dict__)
            .returning(Category)
        )
        result = await self.session.execute(stmt)
        await self.session.commit()
        result_orm = result.scalar_one()
        return CategoryInDB.model_validate(result_orm)

    async def get_all(self, offset: int, limit: int):
        stmt = select(Category).offset(offset).limit(limit)
        result = await self.session.execute(stmt)
        result_orm = result.scalars().all()
        return [CategoryInDB.model_validate(row, from_attributes=True) for row in result_orm]

    async def get_one(self, category_id: int):
        stmt = select(Category).where(Category.id == category_id)
        result = await self.session.execute(stmt)
        result_orm = result.scalar()
        return CategoryInDB.model_validate(result_orm) if result_orm else None

    async def update(
            self, category_id: int, name_category: CategoryCreateDTO
    ):
        stmt = (
            update(Category)
            .where(Category.id == category_id)
            .values(name=name_category.name)
            .returning(Category)
        )
        result = await self.session.execute(stmt)
        await self.session.commit()
        result_orm = result.scalar()
        return CategoryInDB.model_validate(result_orm) if result_orm else None

    async def delete(self, category_id: int):
        stmt = (
            delete(Category)
            .where(Category.id == category_id)
            .returning(Category)
        )
        result = await self.session.execute(stmt)
        await self.session.commit()
        result_orm = result.scalar()
        return CategoryInDB.model_validate(result_orm) if result_orm else None
