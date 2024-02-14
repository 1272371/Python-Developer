from fastapi import Request
from src.logger import logger
import time

async def log_middleware(request: Request, call_next):
    """
    Middleware function that logs the request URL, method, and process time.

    Args:
        request (Request): The incoming request object.
        call_next (Callable): The next middleware or endpoint to call.

    Returns:
        Response: The response object.
    """
    start = time.time()
    response = await call_next(request)
    process_time = time.time() - start

    log_dict ={
        'url': request.url.path,
        'method':request.method,
        'process_time':process_time,
        'body':request.get("events")
    }
    logger.info(log_dict)
    return response
