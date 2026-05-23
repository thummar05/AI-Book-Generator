from services.callback_dependency_service import (
    get_downstream_dependencies
)

from services.glossary_service import (
    rebuild_glossary
)

from services.toc_service import (
    rebuild_toc
)

from services.retrieval_service import (
    retrieve_relevant_context,
    retrieve_callback_candidates
)

from services.character_service import (
    fetch_character_memory
)

from services.llm_regeneration_service import (
    regenerate_chapter_content
)

from memory.database import (
    SessionLocal
)

from graph.nodes.assembler import (
    assembler_node
)


def determine_affected_chapters(
    run_id,
    changed_chapter
):

    dependencies = (
        get_downstream_dependencies(
            run_id=run_id,
            chapter_number=changed_chapter
        )
    )

    affected = set()

    for dep in dependencies:

        affected.add(
            dep["source_chapter"]
        )

    return sorted(
        list(affected)
    )


def rebuild_book_artifacts(
    state
):

    # ==========================================
    # REBUILD GLOSSARY
    # ==========================================

    glossary = rebuild_glossary(
        state["chapters"]
    )

    state["back_matter"][
        "glossary"
    ] = glossary

    # ==========================================
    # REBUILD TABLE OF CONTENTS
    # ==========================================

    toc = rebuild_toc(
        state["chapters"]
    )

    state["front_matter"][
        "table_of_contents"
    ] = toc

    # ==========================================
    # REASSEMBLE FINAL BOOK
    # ==========================================

    state = assembler_node(state)

    return state


def repair_book_continuity(
    state,
    changed_chapter,
    new_content
):

    chapters = state["chapters"]

    # ==========================================
    # VALIDATE CHAPTER
    # ==========================================

    if (
        changed_chapter < 1 or
        changed_chapter > len(chapters)
    ):

        return {

            "updated_state": state,

            "affected_chapters": [],

            "error":
                "Invalid chapter number"
        }

    # ==========================================
    # UPDATE CHANGED CHAPTER
    # ==========================================

    chapters[
        changed_chapter - 1
    ]["content"] = new_content

    # ==========================================
    # FIND AFFECTED CHAPTERS
    # ==========================================

    # Use dependency service to find downstream chapters that need repair
    affected = determine_affected_chapters(
        run_id=state["run_id"],
        changed_chapter=changed_chapter
    )
    # Ensure the changed chapter itself is included
    if changed_chapter not in affected:
        affected.append(changed_chapter)
    # Sort for deterministic order
    affected = sorted(affected)

    print("AFFECTED:", affected)

    db = SessionLocal()

    # ==========================================
    # REGENERATE AFFECTED CHAPTERS
    # ==========================================

    for chapter_num in affected:

        idx = chapter_num - 1

        if idx < 0 or idx >= len(chapters):
            continue

        chapter = chapters[idx]

        print(
            f"Regenerating Chapter {chapter_num}"
        )

        # ======================================
        # MEMORY RETRIEVAL
        # ======================================

        retrieved_context = (
            retrieve_relevant_context(
                chapter["title"],
                run_id=state["run_id"]
            )
        )

        callback_candidates = (
            retrieve_callback_candidates(
                run_id=state["run_id"]
            )
        )

        character_memory = (
            fetch_character_memory(db, run_id=state["run_id"])
        )

        # ======================================
        # BUILD REGEN VARIABLES
        # ======================================

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

        print(
            "Calling LLM regeneration..."
        )

        # ======================================
        # LLM CONTINUITY REGENERATION
        # ======================================

        regenerated_content = (
            regenerate_chapter_content(
                variables
            )
        )

        print(
            "LLM regeneration complete"
        )

        # ======================================
        # UPDATE CHAPTER
        # ======================================

        chapter["content"] = regenerated_content
        # Assuming regenerated_content may include callbacks_used metadata; store callbacks if available
        # Here we store the callbacks_used as an empty list for now (placeholder)
        chapter["callbacks_used"] = []
        # Persist updated chapter memory with callbacks
        from services.retrieval_service import store_chapter_memory
        store_chapter_memory(
            chapter_number=chapter_num,
            chapter_title=chapter["title"],
            summary=chapter.get("summary", ""),
            key_concepts=chapter.get("key_concepts", []),
            callbacks_used=chapter["callbacks_used"],
            run_id=state["run_id"]
        )

    db.close()

    # ==========================================
    # REBUILD BOOK ARTIFACTS
    # ==========================================

    state = rebuild_book_artifacts(
        state
    )

    return {

        "updated_state": state,

        "affected_chapters": affected
    }