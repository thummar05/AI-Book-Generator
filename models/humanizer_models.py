from pydantic import BaseModel
from typing import List


class HumanizerOutput(BaseModel):

    humanized_content: str

    ai_tells_removed: List[str]

    callbacks_added: List[str]