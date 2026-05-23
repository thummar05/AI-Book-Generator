def rebuild_toc(
    chapters
):

    toc = []

    for idx, chapter in enumerate(
        chapters,
        start=1
    ):

        toc.append({

            "chapter_number":
                idx,

            "title":
                chapter["title"]
        })

    return toc