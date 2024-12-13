from fastapi import FastAPI
from api.router import api_router

app = FastAPI()

@app.get("/", summary="Корневой маршрут")
async def root():
    """
    Приветственное сообщение на корневом маршруте.
    """
    return {"message": "Welcome to the Parking API!"}

app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
