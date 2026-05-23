from pydantic import BaseModel


class BookRequest(BaseModel):
    topic: str
    tone: str
    target_audience: str
    chapters: int