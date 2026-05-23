from langchain_core.prompts import ChatPromptTemplate

from prompts.writer_prompt import WRITER_PROMPT

from models.chapter_models import ChapterOutput

from services.llm_service import writer_llm


from services.retrieval_service import (
    store_chapter_memory,
    retrieve_relevant_context,
    retrieve_callback_candidates,
    retrieve_research_context
)

from services.character_service import (
    fetch_character_memory,
    save_character_profiles
)


from memory.database import SessionLocal


def writer_node(state):

    outline = state["outline"]

    generated_chapters = []

    db = SessionLocal()

    for idx, chapter in enumerate(outline["chapters"]):

        retrieved_context = retrieve_relevant_context(
            chapter["title"],
            k=3,
            run_id=state["run_id"]
        )

        research_context = retrieve_research_context(
            query=chapter["title"],
            run_id=state["run_id"]
        )

        formatted_research = "\n\n".join(
            [
                f"Source: {item['source']}\n"
                f"Content: {item['content']}"
                for item in research_context
            ])

        callback_candidates = retrieve_callback_candidates(k=5, run_id=state["run_id"])

        character_memory = fetch_character_memory(db, state["run_id"])

        prompt = ChatPromptTemplate.from_template(
            WRITER_PROMPT
        )

        structured_llm = writer_llm.with_structured_output(
            ChapterOutput
        )

        chain = prompt | structured_llm
        

        result = chain.invoke({

            "book_title": outline["book_title"],

            "book_summary": outline["book_summary"],

            "chapter_title": chapter["title"],

            "chapter_summary": chapter["summary"],

            "research_context": formatted_research,

            "target_audience": state["brief"]["target_audience"],

            "tone_profile": state["tone_profile"],

            "memory_context": "\n\n".join(retrieved_context),

            "callback_candidates": "\n\n".join(callback_candidates),

            "character_memory": "\n\n".join(character_memory)

        })


        generated_chapter = result.model_dump()

        generated_chapters.append(
            generated_chapter
        )

        save_character_profiles(
            db,
            generated_chapter["characters"],
            state["run_id"]
        )

        db.commit()

        store_chapter_memory(
            chapter_number=idx + 1,
            chapter_title=generated_chapter["title"],
            summary=generated_chapter["summary"],
            key_concepts=generated_chapter["key_concepts"],
            callbacks_used=generated_chapter["callbacks_used"],
            run_id=state["run_id"]
        )

    db.close()

    state["chapters"] = generated_chapters


    return state