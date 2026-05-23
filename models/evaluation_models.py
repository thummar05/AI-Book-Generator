from pydantic import BaseModel

from typing import List


class EvaluationIssue(BaseModel):

    issue: str

    severity: str


class EvaluationOutput(BaseModel):

    tone_fidelity_score: float

    humanization_score: float

    structural_score: float

    callback_consistency_score: float

    factual_grounding_score: float

    overall_score: float

    strengths: List[str]

    weaknesses: List[str]

    issues: List[EvaluationIssue]