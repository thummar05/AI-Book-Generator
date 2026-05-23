from langchain_core.prompts import ChatPromptTemplate

from prompts.backmatter_prompt import (
    BACKMATTER_PROMPT
)

from models.backmatter_models import (
    BackMatterOutput
)

from services.llm_service import writer_llm



def backmatter_node(state):

    glossary_terms = []

    for chapter in state["chapters"]:

        glossary_terms.extend(
            chapter.get(
                "glossary_terms",
                []
            )
        )

    prompt = ChatPromptTemplate.from_template(
        BACKMATTER_PROMPT
    )

    structured_llm = writer_llm.with_structured_output(
        BackMatterOutput
    )

    chain = prompt | structured_llm

    result = chain.invoke({

        "book_title":
            state["outline"]["book_title"],

        "book_summary":
            state["outline"]["book_summary"],

        "tone_profile":
            state["tone_profile"],

        "chapters":
            state["chapters"],

        "glossary_terms":
            glossary_terms,

        "fact_checks":
            state["fact_checks"]
    })

    state["back_matter"] = (
        result.model_dump()
    )


    return state