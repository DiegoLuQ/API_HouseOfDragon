from fastapi import APIRouter

from .v1 import base

api_router = APIRouter()

api_router.include_router(
    base.api_router, 
    prefix="/v1"
)