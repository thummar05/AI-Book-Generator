from langchain_core.prompts import (
    ChatPromptTemplate
)

from prompts.evaluator_prompt import (
    EVALUATOR_PROMPT
)

from models.evaluation_models import (
    EvaluationOutput
)

from services.llm_service import (
    judge_llm
)


def evaluate_chapter(
    tone,
    chapter_content
):

    prompt = ChatPromptTemplate.from_template(
        EVALUATOR_PROMPT
    )

    structured_llm = (
        judge_llm.with_structured_output(
            EvaluationOutput
        )
    )

    chain = prompt | structured_llm

    result = chain.invoke({

        "tone": tone,

        "chapter_content":
            chapter_content
    })

    return result.model_dump()