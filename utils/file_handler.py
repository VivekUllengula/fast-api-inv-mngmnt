import os
import json
import aiofiles
from pathlib import Path

DATA_FILE = Path("data/items.json")

async def read_json():
    if not os.path.exists(DATA_FILE):
        return []
    async with aiofiles.open(DATA_FILE, "r") as f:
        content = await f.read()
        if not content.strip():
            return []
        return json.loads(content or [])

async def write_json(data):
    async with aiofiles.open(DATA_FILE, "w") as f:
        await f.write(json.dumps(data, indent=4))