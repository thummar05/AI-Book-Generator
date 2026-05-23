from memory.vector_store import (
    get_book_memory_store,
    get_research_store
)


# =====================================================
# BOOK MEMORY STORAGE
# =====================================================

def store_chapter_memory(
    chapter_number,
    chapter_title,
    summary,
    key_concepts,
    callbacks_used,
    run_id: str
):

    text = f"""
    Chapter Title:
    {chapter_title}

    Summary:
    {summary}

    Key Concepts:
    {', '.join(key_concepts)}

    Callbacks:
    {', '.join(callbacks_used)}
    """

    # Use per‑run Chroma store
    store = get_book_memory_store(run_id)
    store.add_texts(
        texts=[text],
        metadatas=[
            {
                "chapter_number": chapter_number,
                "chapter_title": chapter_title,
                "type": "chapter_memory",
                "run_id": run_id
            }
        ]
    )


# =====================================================
# BOOK MEMORY RETRIEVAL
# =====================================================

def retrieve_relevant_context(
    query,
    run_id: str,
    k=3
):

    store = get_book_memory_store(run_id)
    docs = store.similarity_search(
        query,
        k=k,
        filter={"$and": [{"type": {"$eq": "chapter_memory"}}, {"run_id": {"$eq": run_id}}]}

    )

    return [
        doc.page_content
        for doc in docs
    ]


def retrieve_callback_candidates(run_id: str, k=5):

    store = get_book_memory_store(run_id)
    docs = store.similarity_search(
        "important emotional moments and concepts",
        k=k,
        filter={"$and": [{"type": {"$eq": "chapter_memory"}}, {"run_id": {"$eq": run_id}}]}

    )

    return [
        doc.page_content
        for doc in docs
    ]


# =====================================================
# RESEARCH MEMORY STORAGE
# =====================================================

def store_research_chunk(
    topic,
    content,
    source
):

    # Use default research store
    store = get_research_store('default')
    store.add_texts(
        texts=[content],
        metadatas=[
            {
                "topic": topic,
                "source": source,
                "type": "research"
            }
        ]
    )


# =====================================================
# RESEARCH MEMORY RETRIEVAL
# =====================================================

def retrieve_research_context(
    query,
    k=5,
    run_id=None
):

    store = get_research_store(run_id) if run_id else get_research_store('default')
    docs = store.similarity_search(
        query,
        k=k,
        filter={"type": "research"}
    )

    results = [
        {
            "content": doc.page_content,
            "source": doc.metadata.get(
                "source",
                "Unknown"
            )
        }
        for doc in docs
    ]

    return results