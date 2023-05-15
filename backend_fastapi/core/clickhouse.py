from clickhouse_sqlalchemy import make_session
from core.settings import settings
from sqlalchemy import MetaData, create_engine
from sqlalchemy.ext.declarative import declarative_base

# async not worked (((
# from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
# from sqlalchemy.orm import sessionmaker
# engine = create_async_engine(settings.DATABASE_CLICKHOUSE_URI)
# async_session = sessionmaker(
#     engine, class_=AsyncSession, expire_on_commit=False
# )

# sync
engine = create_engine(settings.DATABASE_CLICKHOUSE_URI.replace('+asynch', ''))
session = make_session(engine)


metadata = MetaData(bind=engine)
Base = declarative_base(metadata=metadata)


async def get_clickhouse_session():
    yield session
