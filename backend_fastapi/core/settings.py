from functools import lru_cache
from pydantic import BaseSettings


class Settings(BaseSettings):
    DATABASE_URI: str = "postgresql+asyncpg://dev:dev@localhost:5432/fastapi"

    class Config:
        env_file = ".env"


@lru_cache
def __get_settings():
    return Settings()


settings = __get_settings()
