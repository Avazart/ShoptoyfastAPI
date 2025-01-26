from fastapi import APIRouter, Depends, HTTPException, Query

from .repositories import ProductCrud
from .schemas import ProductDTO, ProductInDB, ProductWithImagesInDB

router = APIRouter(prefix="/products", tags=["Product"])


@router.post("")
async def product_create(
    data: ProductDTO, crud: ProductCrud = Depends(ProductCrud)
) -> ProductInDB:
    result = await crud.create(new_product=data)
    return result


@router.get("")
async def product_get(
    offset: int = 0,
    limit: int = Query(10, ge=1, le=50),
    crud: ProductCrud = Depends(ProductCrud),
) -> list[ProductWithImagesInDB]:
    result = await crud.get_all(offset, limit)
    return result


@router.get("/{product_id}")
async def product_get_one(
    product_id: int, crud: ProductCrud = Depends(ProductCrud)
) -> ProductWithImagesInDB:
    if result := await crud.get_one(product_id=product_id):
        return result
    raise HTTPException(status_code=404, detail="Product not found")


@router.patch("/{product_id}")
async def product_update(
    product_id: int,
    data: ProductDTO,
    crud: ProductCrud = Depends(ProductCrud),
) -> ProductInDB:
    result = await crud.update(
        product_id=product_id,
        category_id=data.category_id,
        product_name=data.name,
        product_available=data.available,
        product_price=data.price,
        product_description=data.description,
    )
    if result:
        return result
    raise HTTPException(status_code=404, detail="Product not found")


@router.delete("/{product_id}")
async def product_delete(
    product_id: int, crud: ProductCrud = Depends(ProductCrud)
) -> ProductInDB:
    result = await crud.delete(product_id=product_id)
    if result:
        return result
    raise HTTPException(status_code=404, detail="Product not found")
