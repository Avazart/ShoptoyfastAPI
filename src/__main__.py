from fastapi import FastAPI

from src.api import user
from src.api.categories import category
from src.api.images import category_image, product_image
from src.api.products import product

app = FastAPI(title="Gumenyuk_shop")


app.include_router(category.router, prefix="/categories", tags=["Category"])
app.include_router(product.router, prefix="/products", tags=["Product"])
app.include_router(
    category_image.router, prefix="/categories-images", tags=["CategoryImage"]
)
app.include_router(
    product_image.router, prefix="/products-images", tags=["ProductImage"]
)

app.include_router(user.router, prefix="/users", tags=["User"])
