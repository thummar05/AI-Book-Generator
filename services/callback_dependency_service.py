from memory.database import SessionLocal

from memory.schemas import (
    CallbackDependency
)


def store_callback_dependency(
    run_id,
    source_chapter,
    target_chapter,
    callback_text
):

    db = SessionLocal()

    dependency = CallbackDependency(

        run_id=run_id,

        source_chapter=source_chapter,

        target_chapter=target_chapter,

        callback_text=callback_text
    )

    db.add(dependency)

    db.commit()

    db.close()


def get_downstream_dependencies(
    run_id,
    chapter_number
):

    db = SessionLocal()

    dependencies = db.query(
        CallbackDependency
    ).filter(
        CallbackDependency.run_id == run_id,
        CallbackDependency.target_chapter == chapter_number
    ).all()

    results = []

    for item in dependencies:

        results.append({

            "source_chapter":
                item.source_chapter,

            "target_chapter":
                item.target_chapter,

            "callback_text":
                item.callback_text
        })

    db.close()

    return results