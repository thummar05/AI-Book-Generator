import json

from memory.database import SessionLocal

from memory.schemas import (
    BookMemory,
    ChapterMemory,
    CallbackIndex,
    GlossaryTerm
)





def memory_keeper_node(state):

    db = SessionLocal()

    book_memory = BookMemory(
        run_id=state["run_id"],
        topic=state["brief"]["topic"],
        tone=state["brief"]["tone"],
        outline=json.dumps(state["outline"]),
        tone_profile=json.dumps(
            state["tone_profile"]
        )
    )

    db.add(book_memory)

    for idx, chapter in enumerate(state["chapters"]):

        chapter_memory = ChapterMemory(
            run_id=state["run_id"],
            chapter_number=idx + 1,
            chapter_title=chapter["title"],
            summary=chapter["summary"],
            key_concepts=json.dumps(
                chapter["key_concepts"]
            ),
            callbacks_used=json.dumps(
                chapter["callbacks_used"]
            )
        )

        db.add(chapter_memory)

        for callback in chapter["callbacks_used"]:

            callback_record = CallbackIndex(
            run_id=state["run_id"],
            chapter_number=idx + 1,
            callback_text=callback
        )

            db.add(callback_record)


        for glossary_item in chapter["glossary_terms"]:

            glossary_record = GlossaryTerm(
            run_id=state["run_id"],
            term=glossary_item["term"],
            definition=glossary_item["definition"],
            chapter_number=idx + 1
        )

            db.add(glossary_record)





    db.commit()

    db.close()

    return state