from fastapi import APIRouter
from store.controllers.product import router as product
from store.controllers.client import router as client

api_router = APIRouter()
api_router.include_router(product, prefix="/products")
api_router.include_router(client, prefix="/clients")
