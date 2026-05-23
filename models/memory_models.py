from pydantic import BaseModel

from typing import List


class GlossaryItem(BaseModel):

    term: str

    definition: str


class CharacterProfile(BaseModel):

    character_name: str

    traits: List[str]

    relationships: List[str]

    speaking_style: str
