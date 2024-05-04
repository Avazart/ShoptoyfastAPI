from typing import Optional, List, Annotated

from _decimal import Decimal
from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import Field

from src.common.constant.constant import BASE_IMAGE_URL
from src.common.dto.products.product import ProductCreateDTO, ProductInDB
from src.services.database.repositories.product.product import ProductCrud

router = APIRouter()




@router.post("/create")
async def product_create(
    data: ProductCreateDTO, crud: ProductCrud = Depends(ProductCrud)
):
    result = await crud.create(new_product=data)
    return result


@router.get("/list")
async def product_get(
        offset: int = 0,
        limit: int = Query(10, ge=1, le=50),
        crud: ProductCrud = Depends(ProductCrud),
):
    result = await crud.get_all(offset, limit)
    return result


@router.get("/detail/{id}")
async def product_get_one(
    product_id: int, crud: ProductCrud = Depends(ProductCrud)
):
    if result := await crud.get_one(product_id=product_id):
        return result
    raise HTTPException(status_code=404, detail="Product not found")


@router.patch("/update/{id}")
async def product_update(
    product_id: int,
    data: ProductCreateDTO,
    crud: ProductCrud = Depends(ProductCrud),
):
    result = await crud.update(
        product_id=product_id,
        category_id=data.category_id,
        product_name=data.name,
        product_available=data.available,
        product_price=data.price,
        product_description=data.description,
    )
    return result


@router.delete("/delete/{id}")
async def product_delete(
    product_id: int, crud: ProductCrud = Depends(ProductCrud)
):
    result = await crud.delete(product_id=product_id)
    return result
