from sqlalchemy.orm import Session

from memory.schemas import CharacterBible


def save_character_profiles(db: Session, characters, run_id: str):

    for character in characters:

        profile = CharacterBible(
            run_id=run_id,
            character_name=character["character_name"],
            traits=", ".join(character["traits"]),
            relationships=", ".join(character["relationships"]),
            speaking_style=character["speaking_style"]
        )

        db.add(profile)


def fetch_character_memory(db: Session, run_id: str):

    records = db.query(CharacterBible).filter(CharacterBible.run_id == run_id).all()

    memory = []

    for record in records:

        memory.append(f"""
        Character: {record.character_name}
        Traits: {record.traits}
        Relationships: {record.relationships}
        Speaking Style: {record.speaking_style}
        """)

    return memory