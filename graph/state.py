from typing import TypedDict, List, Dict, Any


class BookState(TypedDict):

    run_id: str

    brief: Dict[str, Any]

    outline: Dict[str, Any]

    tone_profile: Dict[str, Any]

    front_matter: Dict[str, Any]

    back_matter: Dict[str, Any]

    research_notes: List[Dict[str, Any]]

    chapters: List[Dict[str, Any]]

    memory: Dict[str, Any]

    fact_checks: List[Dict[str, Any]]

    final_book: str

    evaluations: List[Dict[str, Any]]

    