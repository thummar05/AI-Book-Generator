from pydantic import BaseModel

from typing import List


class GlossaryEntry(BaseModel):

    term: str

    definition: str


class ReferenceEntry(BaseModel):

    title: str

    source: str


class BackMatterOutput(BaseModel):

    afterword: str

    appendix: str

    glossary: List[GlossaryEntry]

    references: List[ReferenceEntry]

    about_author: str

    back_cover_copy: str