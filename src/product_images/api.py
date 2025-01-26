import os.path

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from starlette.responses import FileResponse

from ..file_check import check_file, generate_file_id
from ..settings import IMAGES_DIR
from .repositories import ProductImageCrud, ProductImagesInDB
from .schemas import ProductImagesDTO

router = APIRouter(prefix="/products-images", tags=["ProductImage"])


@router.post("")
async def create_file_product(
    product_id: int,
    file: UploadFile = File(...),
    data: ProductImagesDTO = Depends(),
    crud: ProductImageCrud = Depends(ProductImageCrud),
) -> ProductImagesInDB:
    check_file(file)
    file_id = generate_file_id()
    file_path = IMAGES_DIR + file_id + ".jpeg"
    with open(file_path, "wb") as f:
        f.write(await file.read())
    result = await crud.create(
        file_id=file_id, product_id=product_id, new_image=data
    )
    return result


@router.get("")
async def get_image(
    image_id: int, crud: ProductImageCrud = Depends(ProductImageCrud)
):
    result = await crud.get_one(image_id=image_id)
    if result and os.path.isfile(IMAGES_DIR + result.file_id + ".jpeg"):
        return FileResponse(IMAGES_DIR + result.file_id + ".jpeg")
    raise HTTPException(status_code=404, detail="Image not found")


@router.delete("/{image_id}")
async def image_delete(
    image_id: int, crud: ProductImageCrud = Depends(ProductImageCrud)
) -> ProductImagesInDB:
    result = await crud.delete(image_id=image_id)
    if result:
        return result
    raise HTTPException(status_code=404, detail="Image not found")
