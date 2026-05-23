def assembler_node(state):

    outline = state["outline"]

    front = state["front_matter"]

    back = state["back_matter"]

    book_parts = []


    book_parts.append("[SECTION:HALF_TITLE]")
    book_parts.append(front["half_title"])


    book_parts.append("[SECTION:TITLE_PAGE]")
    book_parts.append(front["title_page"])


    book_parts.append("[SECTION:COPYRIGHT]")
    book_parts.append(front["copyright_page"])


    book_parts.append("[SECTION:DEDICATION]")
    book_parts.append(front["dedication"])


    book_parts.append("[SECTION:EPIGRAPH]")
    book_parts.append(front["epigraph"])


    book_parts.append("[SECTION:TOC]")

    for item in front["table_of_contents"]:

        book_parts.append(
            f"Chapter {item['chapter_number']}: "
            f"{item['title']}"
        )


    book_parts.append("[SECTION:PREFACE]")
    book_parts.append(front["preface"])


    book_parts.append("[SECTION:ACKNOWLEDGMENTS]")
    book_parts.append(front["acknowledgments"])


    book_parts.append("[SECTION:INTRODUCTION]")
    book_parts.append(front["introduction"])


    for idx, chapter in enumerate(
        state["chapters"],
        start=1
    ):

        book_parts.append(
            f"[CHAPTER:{idx}]"
        )

        book_parts.append(
            f"[CHAPTER_TITLE]"
            f"{chapter['title']}"
            f"[/CHAPTER_TITLE]"
        )

        book_parts.append(
            chapter["content"]
        )


    book_parts.append("[SECTION:AFTERWORD]")
    book_parts.append(back["afterword"])


    book_parts.append("[SECTION:APPENDIX]")
    book_parts.append(back["appendix"])


    book_parts.append("[SECTION:GLOSSARY]")

    for item in back["glossary"]:

        book_parts.append(
            f"[TERM]{item['term']}[/TERM]"
        )

        book_parts.append(
            f"[DEF]{item['definition']}[/DEF]"
        )


    book_parts.append("[SECTION:REFERENCES]")

    for item in back["references"]:

        book_parts.append(
            f"{item['title']} — "
            f"{item['source']}"
        )


    book_parts.append("[SECTION:ABOUT_AUTHOR]")
    book_parts.append(back["about_author"])


    book_parts.append("[SECTION:BACK_COVER]")
    book_parts.append(back["back_cover_copy"])



    final_book = "\n\n".join(book_parts)

    state["final_book"] = final_book


    return state