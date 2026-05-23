from services.evaluation_service import (
    evaluate_chapter
)


def evaluator_node(state):

    evaluations = []

    tone = state["brief"]["tone"]

    for chapter in state["chapters"]:

        evaluation = evaluate_chapter(

            tone=tone,

            chapter_content=chapter[
                "content"
            ]
        )

        evaluations.append({

            "chapter":
                chapter["title"],

            "evaluation":
                evaluation
        })

    state["evaluations"] = evaluations

    return state