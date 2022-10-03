from fastapi import APIRouter
from .routes_character import router as routes_character

api_router = APIRouter()

api_router.include_router(
    routes_character,
    prefix="/character",
    tags=["Characters"]
)
