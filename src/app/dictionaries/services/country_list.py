import sqlalchemy as sa
from sqlalchemy.ext.asyncio import AsyncSession

from app.dictionaries.models import CountryEntity
from app.dictionaries.schemas.country import CountryDomain
from core.database import get_session


async def country_list(session: AsyncSession) -> list[CountryDomain]:
    session = await get_session()
    sql = sa.select(CountryEntity).order_by(CountryEntity.countryName.desc())
    result = await session.execute(sql)
    countries = result.scalars().all()
    return [
        CountryDomain(
            **{field: getattr(country, field) for field in CountryDomain.__fields__}
        )
        for country in countries
    ]


async def country_detail(session: AsyncSession, pk: int) -> CountryDomain:
    sql = (
        sa.select(CountryEntity)
        .order_by(CountryEntity.countryName.desc())
        .where(CountryEntity.id == pk)
    )
    result = await session.execute(sql)
    country = result.scalars().first()
    return CountryDomain(
        **{field: getattr(country, field) for field in CountryDomain.__fields__}
    )
