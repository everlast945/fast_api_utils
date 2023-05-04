from core.database import engine
from apps.items.entity.item import *


async def recreate_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
