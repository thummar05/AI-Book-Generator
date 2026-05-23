from pydantic import BaseModel

from typing import List


class Citation(BaseModel):

    title: str

    source: str

    excerpt: str


class ResearchChunk(BaseModel):

    topic: str

    content: str

    citations: List[Citation]