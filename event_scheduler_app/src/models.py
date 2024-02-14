from pydantic import BaseModel, validator
import re

class Event(BaseModel):
    title: str
    description: str
    date: str
    time: str

    @validator('date')
    def validate_date_format(cls, v):
        if not re.fullmatch(r'\d{4}-\d{2}-\d{2}', v):
            raise ValueError('Invalid date format. Date should be in YYYY-MM-DD format.')
        return v

    @validator('time')
    def validate_time_format(cls, v):
        if not re.fullmatch(r'\d{2}:\d{2}', v):
            raise ValueError('Invalid time format. Time should be in HH:MM format.')
        return v