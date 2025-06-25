from fastapi import FastAPI
from services.item_service import ItemService
from models.item_model import Item
from utils.decorators import log_time
import asyncio

app =FastAPI()
item_service = ItemService()

@app.get("/api/items")
@log_time
async def get_items():
    return await item_service.get_all_items()

@app.get("/api/items/{item_id}")
async def get_item(item_id: str):
    return await item_service.get_item_by_id(item_id)

@app.post("/api/items")
async def create_item(item: Item):
    return await item_service.create_item(item)

@app.put("/api/items/{item_id}")
async def update_item(item_id: str, item: Item):
    return await item_service.update_item(item_id, item)
