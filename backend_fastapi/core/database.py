from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession


SQLALCHEMY_DATABASE_URL = "postgresql+asyncpg://dev:dev@localhost:5432/films_main"

engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True)
async_session = async_sessionmaker(engine, expire_on_commit=False)


Base = declarative_base()


async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session

