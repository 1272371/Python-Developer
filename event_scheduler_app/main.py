from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import List
import uvicorn

from starlette.middleware.base import BaseHTTPMiddleware
from src.middleware import log_middleware
from src.models import Event 
from src.logger import logger

# FastAPI
app = FastAPI()
app.add_middleware(BaseHTTPMiddleware, dispatch=log_middleware)

# Test the logger
logger.info('Starting the Fast API app ...')

# In-memory database to store events
events_db = []

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Template rendering
templates = Jinja2Templates(directory="templates")

# Routes and API
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """
    Home Page
    """
    logger.info('Rendering the home page ...')
    return templates.TemplateResponse("index.html", request=request, context={"request": request, "events": events_db})

@app.get("/api/events/{title}", response_model=Event)
async def get_event(title: str):
    """
    Get an event by title.
    """
    logger.info('Getting an event ...')
    global events_db
    for event in events_db:
        if event["title"] == title:
            return event
    raise HTTPException(status_code=404, detail="Event not found")

@app.get("/api/events/", response_model=List[Event])
async def list_events():
    """
    List all events.
    """
    logger.info('Listing all events ...')
    return events_db

@app.post("/api/events/")
async def add_event(event: Event):
    """
    Add a new event.
    """
    logger.info('Adding a new event ...')
    try:
        events_db.append(event.dict())
        return {"message": "Event added successfully", "events": events_db}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.delete("/api/events/{title}")
async def delete_event(title: str):
    """
    Delete an event by title.
    """
    logger.info('Deleting an event ...')
    global events_db
    initial_length = len(events_db)
    events_db = [event for event in events_db if event.title != title]
    if len(events_db) == initial_length:
        raise HTTPException(status_code=404, detail="Event not found")
    return {"message": "Event deleted successfully", "events": events_db}

@app.put("/api/events/{title}")
async def update_event(title: str, updated_event: Event):
    """
    Update an event by title.
    """
    logger.info('Updating an event ...')
    for event in events_db:
        if event.title == title:
            event.title = updated_event.title
            event.description = updated_event.description
            event.date = updated_event.date
            return {"message": "Event updated successfully", "event": event}
    raise HTTPException(status_code=404, detail="Event not found")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
