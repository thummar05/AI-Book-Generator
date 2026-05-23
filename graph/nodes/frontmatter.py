from langchain_core.prompts import ChatPromptTemplate

from prompts.frontmatter_prompt import (
    FRONTMATTER_PROMPT
)

from models.frontmatter_models import (
    FrontMatterOutput
)

from services.llm_service import writer_llm



def frontmatter_node(state):

    outline = state["outline"]

    prompt = ChatPromptTemplate.from_template(
        FRONTMATTER_PROMPT
    )

    structured_llm = writer_llm.with_structured_output(
        FrontMatterOutput
    )

    chain = prompt | structured_llm

    result = chain.invoke({

        "topic":
            state["brief"]["topic"],

        "book_title":
            outline["book_title"],

        "book_summary":
            outline["book_summary"],

        "target_audience":
            state["brief"]["target_audience"],

        "tone_profile":
            state["tone_profile"],

        "chapters":
            outline["chapters"]
    })

    state["front_matter"] = (
        result.model_dump()
    )
    return state