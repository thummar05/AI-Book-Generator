from langchain_core.prompts import ChatPromptTemplate

from prompts.editor_prompt import (
    EDITOR_PROMPT
)

from models.editor_models import (
    EditorOutput
)

from services.llm_service import editor_llm



def editor_node(state):

    updated_chapters = []

    for chapter in state["chapters"]:

        prompt = ChatPromptTemplate.from_template(
            EDITOR_PROMPT
        )

        structured_llm = editor_llm.with_structured_output(
            EditorOutput
        )

        chain = prompt | structured_llm

        result = chain.invoke({

            "chapter_content":
                chapter["content"]
        })

        chapter["content"] = (
            result.edited_content
        )

        updated_chapters.append(chapter)

    state["chapters"] = updated_chapters


    return state