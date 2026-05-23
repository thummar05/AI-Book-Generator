from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Text

Base = declarative_base()


class BookMemory(Base):
    __tablename__ = "book_memory"
    id = Column(Integer, primary_key=True)
    run_id = Column(String)
    topic = Column(String)
    tone = Column(String)
    outline = Column(Text)
    tone_profile = Column(Text)


class ChapterMemory(Base):
    __tablename__ = "chapter_memory"
    id = Column(Integer, primary_key=True)
    run_id = Column(String)
    chapter_number = Column(Integer)
    chapter_title = Column(String)
    summary = Column(Text)
    key_concepts = Column(Text)
    callbacks_used = Column(Text)


class CallbackIndex(Base):
    __tablename__ = "callback_index"
    id = Column(Integer, primary_key=True)
    run_id = Column(String)
    chapter_number = Column(Integer)
    callback_text = Column(Text)


class GlossaryTerm(Base):
    __tablename__ = "glossary_terms"
    id = Column(Integer, primary_key=True)
    run_id = Column(String)
    chapter_number = Column(Integer)
    term = Column(String)
    definition = Column(Text)


class CharacterBible(Base):
    __tablename__ = "character_bible"
    id = Column(Integer, primary_key=True)
    run_id = Column(String)
    character_name = Column(String)
    traits = Column(Text)
    relationships = Column(Text)
    speaking_style = Column(Text)


class CallbackDependency(Base):
    __tablename__ = "callback_dependencies"
    id = Column(Integer, primary_key=True)
    run_id = Column(String)
    source_chapter = Column(Integer)
    target_chapter = Column(Integer)
    callback_text = Column(Text)