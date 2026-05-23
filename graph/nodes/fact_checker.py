from langchain_core.prompts import ChatPromptTemplate

from prompts.fact_checker_prompt import (
    FACT_CHECKER_PROMPT
)

from models.fact_checker_models import (
    FactCheckerOutput
)

from services.llm_service import editor_llm


from services.retrieval_service import (
    retrieve_research_context
)


def fact_checker_node(state):

    updated_chapters = []

    all_fact_checks = []

    for chapter in state["chapters"]:

        research_context = retrieve_research_context(
            query=chapter["title"],
            run_id=state["run_id"]
        )

        prompt = ChatPromptTemplate.from_template(
            FACT_CHECKER_PROMPT
        )

        structured_llm = editor_llm.with_structured_output(
            FactCheckerOutput
        )

        chain = prompt | structured_llm
        formatted_research = "\n\n".join(

            [
                f"Source: {item['source']}\n"
                f"Content: {item['content']}"
                for item in research_context
            ]
        )

        result = chain.invoke({
            "research_context": formatted_research,
            "chapter_content":
                chapter["content"]
        })

        chapter["content"] = (
            result.revised_content
        )

        updated_chapters.append(chapter)

        all_fact_checks.extend(
            [
                item.model_dump()
                for item in result.fact_checks
            ]
        )

    state["chapters"] = updated_chapters

    state["fact_checks"] = all_fact_checks


    return state