from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# In-memory database to store events
events_db = []

# Pydantic model for Event
class Event(BaseModel):
    title: str
    description: str
    date: str
    time: str

# Routes for adding, listing, deleting, and editing events
@app.post("/")
def add_event(event: Event):
    try:
        events_db.append(event.dict())
        return {"message": "Event added successfully"}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {e}"}

@app.get("/", response_model=List[Event])
def list_events():
    try:
        return events_db
    except Exception as e:
        return {"error": f"An unexpected error occurred: {e}"}

@app.delete("/{title}/")
def delete_event(title: str):
    try:
        global events_db
        initial_length = len(events_db)
        events_db = [event for event in events_db if event.title != title]
        if len(events_db) == initial_length:
            raise HTTPException(status_code=404, detail="Event not found")
        return {"message": "Event deleted successfully"}
    except HTTPException as http_exc:
        return {"error": f"HTTP Exception: {http_exc.detail}"}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {e}"}
