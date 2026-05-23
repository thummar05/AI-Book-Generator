from pydantic import BaseModel
from typing import List


class EditorOutput(BaseModel):

    edited_content: str

    edits_made: List[str]