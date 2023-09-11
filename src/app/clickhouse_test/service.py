import clickhouse_connect
import sqlalchemy as sa
from sqlalchemy.ext.asyncio import AsyncSession

from app.clickhouse_test.models import CountryEntity
from app.dictionaries.schemas.country import CountryDomain
from app.leonardo.factories import (
    CabinAvailabilityHistoryFactory,
    LegAvailabilityHistoryFactory,
    SubclassAvailabilityHistoryFactory,
)
from app.leonardo.models import (
    CabinAvailabilityHistory,
    LegAvailabilityHistory,
    SubclassAvailabilityHistory,
)
from core.clickhouse import Base


async def country_clickhouse_list(session: AsyncSession) -> list[CountryDomain]:
    sql = sa.select(CountryEntity).order_by(CountryEntity.countryName.desc())
    result = await session.execute(sql)
    countries = result.scalars().all()
    return [
        CountryDomain(
            **{field: getattr(country, field) for field in CountryDomain.__fields__}
        )
        for country in countries
    ]


class GenerateFakeData:
    def __init__(self) -> None:
        super().__init__()
        self.client = clickhouse_connect.get_client(
            host='localhost', port=8123, database='fastapi'
        )

    async def run(self):
        # self._recrete_tables()

        bulk = LegAvailabilityHistoryFactory.create_batch(10)
        leg_ids = (x for x in self._bulk_create(bulk, LegAvailabilityHistory))
        bulk = [
            item
            for leg_id in leg_ids
            for item in CabinAvailabilityHistoryFactory.create_batch(
                10, LegAvailabilityId=leg_id
            )
        ]
        cabin_ids = (x for x in self._bulk_create(bulk, CabinAvailabilityHistory))
        bulk = [
            item
            for cabin_id in cabin_ids
            for item in SubclassAvailabilityHistoryFactory.create_batch(
                10, CabinAvailabilityId=cabin_id
            )
        ]
        self._bulk_create(bulk, SubclassAvailabilityHistory)
        sql = sa.select(sa.func.count(SubclassAvailabilityHistory.uid)).select_from(
            SubclassAvailabilityHistory
        )
        result = self.client.command(str(sql))
        print(f'result: {result}')

    def _recrete_tables(self):
        for table in (
            LegAvailabilityHistory,
            CabinAvailabilityHistory,
            SubclassAvailabilityHistory,
        ):
            try:
                table.__table__.drop()
            except Exception:
                pass
            table.__table__.create()

    def _bulk_create(self, bulk: list[dict], table: Base):
        data = [tuple(x.values()) for x in bulk]
        self.client.insert(
            table=str(str(table.__tablename__)),
            data=data,
            column_names=list(bulk[0].keys()),
        )
        return [x[0] for x in data]
