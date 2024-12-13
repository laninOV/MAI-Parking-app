from fastapi import APIRouter
from api.v1.parking_router import parking_router

#основной роутер
api_router = APIRouter()

#подключение роутера парковок
api_router.include_router(parking_router, prefix="/v1/parking", tags=["Parking"])
