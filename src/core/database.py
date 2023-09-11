from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from core.settings import settings

engine = create_async_engine(settings.DATABASE_URI, echo=True)
# 1.4.48
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
# 2.0
# async_session = async_sessionmaker(engine, expire_on_commit=False)
Base = declarative_base()


async def get_session() -> AsyncSession:
    async with async_session() as session:
        return session
