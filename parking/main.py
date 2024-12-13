from fastapi import FastAPI
from fastapi.responses import JSONResponse
import os
import json

# Инициализация приложения
app = FastAPI()

# Путь к JSON файлу
DATA_FILE = "data.json"

@app.get("/data", response_class=JSONResponse)
async def get_data():
    """
    Ручка для возврата содержимого JSON файла.
    """
    if not os.path.exists(DATA_FILE):
        return JSONResponse(content={"error": "File not found"}, status_code=404)

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)
    return JSONResponse(content=data)
