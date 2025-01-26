from fastapi import FastAPI

from . import categories, category_images, product_images, products, users

app = FastAPI(title="Gumenyuk_shop")

app.include_router(categories.router)
app.include_router(products.router)
app.include_router(category_images.router)
app.include_router(product_images.router)
app.include_router(users.router)
