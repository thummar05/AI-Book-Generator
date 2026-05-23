import os
from langchain_openai import OpenAIEmbeddings

from langchain_chroma import Chroma


embeddings = OpenAIEmbeddings()

def get_book_memory_store(run_id: str):
    """Return a Chroma collection scoped to a specific run_id.
    Each run gets its own collection and persistence directory to prevent cross‑run contamination.
    """
    collection_name = f"book_memory_{run_id}"
    persist_dir = os.path.join(os.getcwd(), "chroma_db", run_id)
    os.makedirs(persist_dir, exist_ok=True)
    return Chroma(
        collection_name=collection_name,
        embedding_function=embeddings,
        persist_directory=persist_dir,
    )

def get_research_store(run_id: str):
    """Return a Chroma collection for research memory scoped to a run_id."""
    collection_name = f"research_memory_{run_id}"
    persist_dir = os.path.join(os.getcwd(), "chroma_db", run_id)
    os.makedirs(persist_dir, exist_ok=True)
    return Chroma(
        collection_name=collection_name,
        embedding_function=embeddings,
        persist_directory=persist_dir,
    )

# Backward compatibility globals (not used in new code)
book_memory_store = None
research_store = None