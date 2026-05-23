from services.chunking_service import (
    chunk_text
)

from services.retrieval_service import (
    store_research_chunk
)


def ingest_research(
    topic,
    source,
    content
):

    chunks = chunk_text(content)

    for chunk in chunks:

        store_research_chunk(
            topic=topic,
            content=chunk,
            source=source
        )