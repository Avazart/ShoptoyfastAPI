
from fastapi import APIRouter, Depends, Query
from fastapi.exceptions import HTTPException

from src.common.dto.category.category import (
    CategoryDTO,
    CategoryInDB,
    CategoryWithImagesInDB,
)
from src.services.database.repositories.categories.category import CategoryCrud

router = APIRouter()


@router.post("")
async def category_create(
    data: CategoryDTO, crud: CategoryCrud = Depends(CategoryCrud)
) -> CategoryInDB:
    result = await crud.create(new_category=data)
    return result


@router.get("")
async def category_get(
    offset: int = 0,
    limit: int = Query(10, ge=1, le=50),
    crud: CategoryCrud = Depends(CategoryCrud),
) -> list[CategoryWithImagesInDB]:
    result = await crud.get_all(offset, limit)
    return result


@router.get("/{category_id}")
async def category_get_one(
    data: int, crud: CategoryCrud = Depends(CategoryCrud)
) -> CategoryWithImagesInDB:
    result = await crud.get_one(category_id=data)
    if result:
        return result
    raise HTTPException(status_code=404, detail="Category not found")


@router.patch("/{category_id}")
async def update(
    category_id: int,
    data: CategoryDTO,
    crud: CategoryCrud = Depends(CategoryCrud),
) -> CategoryInDB:
    result = await crud.update(category_id=category_id, name_category=data)
    if result:
        return result
    raise HTTPException(status_code=404, detail="Category not found")


@router.delete("/{category_id}")
async def delete(
    category_id: int, crud: CategoryCrud = Depends(CategoryCrud)
) -> CategoryInDB:
    result = await crud.delete(category_id=category_id)
    if result:
        return result
    raise HTTPException(status_code=404, detail="Product not found")
