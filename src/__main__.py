from fastapi import FastAPI


from src.api.product import product
from src.api.category import category
from src.api.image import category_image, product_image

app = FastAPI(title="Gumenyuk_shop")


app.include_router(category.router, prefix="/categories", tags=["Category"])
app.include_router(product.router, prefix="/products", tags=["Product"])
app.include_router(
    category_image.router, prefix="/category-images", tags=["CategoryImage"]
)
app.include_router(
    product_image.router, prefix="/product-images", tags=["ProductImage"]
)
