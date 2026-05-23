from services.repair_service import (
    determine_affected_chapters,
    rebuild_book_artifacts
)

from services.llm_regeneration_service import (
    regenerate_chapter_content
)

from services.retrieval_service import (
    retrieve_relevant_context,
    retrieve_callback_candidates
)

from services.character_service import (
    fetch_character_memory
)

from memory.database import (
    SessionLocal
)

from graph.nodes.assembler import (
    assembler_node
)


def prepare_regeneration_plan(
    run_id,
    changed_chapter
):

    affected = (
        determine_affected_chapters(
            run_id=run_id,
            changed_chapter=changed_chapter
        )
    )

    return {

        "changed_chapter":
            changed_chapter,

        "affected_chapters":
            affected
    }


def regenerate_affected_chapters(
    state,
    changed_chapter,
    new_content
):

    # ==========================================
    # REPLACE CHANGED CHAPTER
    # ==========================================

    state["chapters"][
        changed_chapter - 1
    ]["content"] = new_content

    # ==========================================
    # FIND AFFECTED CHAPTERS
    # ==========================================

    affected = determine_affected_chapters(

        run_id=state["run_id"],

        changed_chapter=changed_chapter
    )

    # ==========================================
    # SIMPLE REGENERATION PLACEHOLDER
    # ==========================================

    for chapter_num in affected:

        idx = chapter_num - 1

        chapter = state["chapters"][idx]

        db = SessionLocal()

        retrieved_context = (
            retrieve_relevant_context(
                chapter["title"]
            )
        )

        callback_candidates = (
            retrieve_callback_candidates()
        )

        character_memory = (
            fetch_character_memory(db)
        )

        variables = {

            "book_title":
                state["outline"][
                    "book_title"
                ],

            "chapter_title":
                chapter["title"],

            "original_content":
                chapter["content"],

            "changed_chapter":
                changed_chapter,

            "updated_content":
                new_content,

            "tone_profile":
                state["tone_profile"],

            "memory_context":
                "\n\n".join(
                    retrieved_context
                ),

            "callback_candidates":
                "\n\n".join(
                    callback_candidates
                ),

            "character_memory":
                "\n\n".join(
                    character_memory
                )
        }

        updated_content = (
            regenerate_chapter_content(
                variables
            )
        )

        chapter["content"] = (
            updated_content
        )

        chapter["content"] = updated_content

        db.close()



    # ==========================================
    # REBUILD ARTIFACTS
    # ==========================================

    state = rebuild_book_artifacts(
        state
    )

    state = assembler_node(state)

    return {

        "updated_state": state,

        "affected_chapters": affected
    }