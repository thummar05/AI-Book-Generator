def rebuild_glossary(
    chapters
):

    glossary = []

    seen_terms = set()

    for chapter in chapters:

        for item in chapter.get(
            "glossary_terms",
            []
        ):

            term = item["term"]

            if term not in seen_terms:

                glossary.append(item)

                seen_terms.add(term)

    return glossary