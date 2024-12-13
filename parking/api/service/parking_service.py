import json
import os

#путь к JSON файлу
DATA_FILE = "data.json"

async def get_parking_data():
    """
    Бизнес-логика получения списка парковок.
    """
    if not os.path.exists(DATA_FILE):
        return {"error": "File not found"}

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data
