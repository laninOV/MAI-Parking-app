from fastapi import APIRouter
from api.service.parking_service import get_parking_data
from fastapi.responses import JSONResponse

parking_router = APIRouter()

@parking_router.get("/", summary="Получение списка парковок")
async def get_parking():
    """
    Возвращает список парковок из сервиса.
    """
    parking_data = await get_parking_data()
    if "error" in parking_data:
        return JSONResponse(content=parking_data, status_code=404)
    
    return JSONResponse(content=parking_data)
