from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    OPENAI_API_KEY: str

    LANGCHAIN_API_KEY: str

    LANGCHAIN_TRACING_V2: bool = True

    LANGCHAIN_PROJECT: str = "ai-book-generator"

    class Config:
        env_file = ".env"


settings = Settings()