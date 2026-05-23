from pydantic import BaseModel
from typing import List


class ChapterOutline(BaseModel):

    chapter_number: int

    title: str

    summary: str


class PlannerOutput(BaseModel):

    book_title: str

    book_summary: str

    chapters: List[ChapterOutline]