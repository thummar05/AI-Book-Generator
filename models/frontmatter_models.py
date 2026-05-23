from pydantic import BaseModel

from typing import List


class TOCEntry(BaseModel):

    chapter_number: int

    title: str


class FrontMatterOutput(BaseModel):

    half_title: str

    title_page: str

    copyright_page: str

    dedication: str

    epigraph: str

    table_of_contents: List[TOCEntry]

    preface: str

    acknowledgments: str

    introduction: str