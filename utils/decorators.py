import time
import logging
from functools import wraps

logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO
)

def log_time(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        start = time.time()
        response = await func(*args, **kwargs)
        end = time.time()
        logging.info(f"{func.__name__} took {end - start:.4f} seconds")
        return response
    return wrapper