import json
from pathlib import Path

DATA_FILE = Path("data/items.json")

async def read_json():
    if not DATA_FILE.exists():
        return []
    async with open(DATA_FILE, "r") as f:
        content = await f.read()
        return json.loads(content or [])

async def write_json(data):
    with open(DATA_FILE, "w") as f:
        await f.write(json.dumps(data, indent=4))