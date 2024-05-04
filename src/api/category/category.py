
from fastapi import APIRouter, Depends, Query
from fastapi.exceptions import HTTPException
from sqlalchemy.exc import IntegrityError

from src.common.dto.category.category import CategoryCreateDTO, CategoryInDB
from src.services.database.repositories.category.category import CategoryCrud

router = APIRouter()


@router.post("/create")
async def category_create(
    data: CategoryCreateDTO, crud: CategoryCrud = Depends(CategoryCrud)
):
    try:
        result = await crud.create(new_category=data)
        return result
    except IntegrityError:
        raise HTTPException(status_code=403, detail="Category exists")


@router.get("/list")
async def category_get(
        offset: int = 0,
        limit: int = Query(10, ge=1, le=50),
        crud: CategoryCrud = Depends(CategoryCrud),
):
    result = await crud.get_all(offset, limit)
    return result


@router.get("/detail/{id}")
async def category_get_one(
    data: int, crud: CategoryCrud = Depends(CategoryCrud)
):
    result = await crud.get_one(category_id=data)
    if result:
        return result
    raise HTTPException(status_code=404, detail="Category not found")


@router.patch("/update/{id}")
async def update(
    category_id: int,
    data: CategoryCreateDTO,
    crud: CategoryCrud = Depends(CategoryCrud),
):
    result = await crud.update(category_id=category_id, name_category=data)
    return result


@router.delete("/delete/{id}")
async def delete(
    category_id: int, crud: CategoryCrud = Depends(CategoryCrud)
):
    result = await crud.delete(category_id=category_id)
    return result
