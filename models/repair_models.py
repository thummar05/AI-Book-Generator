from pydantic import BaseModel
from typing import List


class RepairRequest(BaseModel):

    changed_chapter: int

    new_content: str
