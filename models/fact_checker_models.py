from pydantic import BaseModel

from typing import List


class Evidence(BaseModel):

    source: str

    excerpt: str


class FactCheckItem(BaseModel):

    claim: str

    verdict: str

    action: str

    confidence: float

    evidence: List[Evidence]


class FactCheckerOutput(BaseModel):

    revised_content: str

    fact_checks: List[FactCheckItem]