from typing import Optional, List

from fastapi import APIRouter, Depends, HTTPException

from src.common.constant.constant import BASE_IMAGE_URL
from src.common.dto.products.product import ProductCreateDTO, ProductInDB
from src.services.database.repositories.product.product import ProductCrud

router = APIRouter()


@router.post("/create")
async def product_create(
    data: ProductCreateDTO, crud: ProductCrud = Depends(ProductCrud)
) -> ProductInDB:
    result = await crud.create(new_product=data)
    return result


@router.get("/list")
async def product_get(
    crud: ProductCrud = Depends(ProductCrud),
) -> List[ProductInDB] | None:
    result = await crud.get_all()
    return result


@router.get("/detail/{id}")
async def product_get_one(
    product_id: int, crud: ProductCrud = Depends(ProductCrud)
) -> Optional[ProductInDB]:
    result = await crud.get_one(product_id=product_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Product not found")
    image_links = [
        {
            "id": image.id,
            "link": f"{BASE_IMAGE_URL}{image.id}",
            "main": image.is_main_image,
        }
        for image in result.images
    ]
    result.image_links = image_links
    return result


@router.patch("/update/{id}")
async def product_update(
    product_id: int,
    data: ProductCreateDTO,
    crud: ProductCrud = Depends(ProductCrud),
) -> ProductInDB | None:
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
) -> Optional[ProductInDB]:
    result = await crud.delete(product_id=product_id)
    return result
