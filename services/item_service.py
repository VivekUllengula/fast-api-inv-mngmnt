from utils.file_handler import read_json,write_json
from models.item_model import Item
from datetime import datetime
from utils.exceptions import (
    ItemNotFoundException,
    ItemAlreadyExistsException
)
class ItemService:
    async def get_all_items(self):
        return await read_json()
    
    async def get_item_by_id(self, item_id):
        items = await read_json()
        for item in items: 
            if item["id"] == item_id:
                return item
        raise ItemNotFoundException()
    
    async def create_item(self, item: Item):
        items = await read_json()
        for x in items:
            if x["id"] == item.id:
                raise ItemAlreadyExistsException()
        item.created_at = datetime.now()
        item_dict = item.dict()
        item_dict["created_at"] = item.created_at.isoformat()
        items.append(item_dict)
        await write_json(items)
        return item
    
    async def update_item(self, item_id, updated_item: Item):
        items = await read_json()
        for i, item in enumerate(items):
            if item["id"] == item_id:
                updated_item.created_at = item["created_at"]
                items[i] = updated_item.dict()
                await write_json(items)
                return updated_item
        raise ItemNotFoundException()
    
    async def delete_item(self, item_id):
        items = await read_json()
        items = [item for item in items if item["id"] != item_id]
        await write_json(items)
        return {"message": f"Item {item_id} deleted"}

    