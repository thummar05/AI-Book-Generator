from services.research_service import (
    ingest_research
)


def researcher_node(state):

    outline = state["outline"]

    research_notes = []

    for chapter in outline["chapters"]:

        chapter_title = chapter["title"]

        # ==========================================
        # TEMP MOCK RESEARCH SOURCE
        # ==========================================

        research_content = f"""
        {chapter_title}

        Personal finance requires understanding
        budgeting, savings, debt management,
        emergency funds, and long-term investing.

        Young professionals benefit from:
        - tracking expenses
        - reducing impulse spending
        - automating savings
        - investing early
        - avoiding high-interest debt

        Financial habits compound over time.
        """

        source = (
            "Internal Finance Knowledge Base"
        )

        # ==========================================
        # INGEST INTO VECTOR STORE
        # ==========================================

        ingest_research(
            topic=chapter_title,
            source=source,
            content=research_content
        )

        research_notes.append({

            "chapter": chapter_title,

            "source": source,

            "summary":
                "Research ingested successfully"
        })

    state["research_notes"] = research_notes


    return state