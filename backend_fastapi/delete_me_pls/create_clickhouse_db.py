import asyncio

from core.clickhouse import Base, engine


class CreateClickhouseDatabase:
    def __init__(self) -> None:
        super().__init__()
        Base.metadata.drop_all()
        Base.metadata.create_all()

    async def run(self):
        # await self._init_models()
        pass

    async def _init_models(self):
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)


if __name__ == '__main__':
    asyncio.run(CreateClickhouseDatabase().run())
