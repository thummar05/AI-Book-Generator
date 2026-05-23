from pydantic import BaseModel

from typing import List

from models.memory_models import (
    GlossaryItem,
    CharacterProfile
)


class ChapterOutput(BaseModel):

    title: str

    summary: str

    content: str

    key_concepts: List[str]

    callbacks_used: List[str]

    glossary_terms: List[GlossaryItem]

    characters: List[CharacterProfile]