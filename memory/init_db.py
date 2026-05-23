from memory.database import engine
from memory.schemas import Base


def init_db():
    
    # Drop all existing tables to ensure schema is up‑to‑date (useful during development)
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)