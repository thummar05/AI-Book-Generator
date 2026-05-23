from langchain_core.prompts import (
    ChatPromptTemplate
)

from prompts.regeneration_prompt import (
    REGENERATION_PROMPT
)

from services.llm_service import (
    writer_llm
)


def regenerate_chapter_content(
    variables
):

    prompt = ChatPromptTemplate.from_template(
        REGENERATION_PROMPT
    )

    chain = prompt | writer_llm

    result = chain.invoke(
        variables
    )

    return result.content