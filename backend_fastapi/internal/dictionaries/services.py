import sqlalchemy as sa
from sqlalchemy.ext.asyncio import AsyncSession

from entity.dictionaries import CountryEntity, GenreEntity, ProfessionEntity
from internal.dictionaries.domain import CountryDomain, GenreDomain, ProfessionDomain


async def country_list(session: AsyncSession) -> list[CountryDomain]:
    sql = sa.select(
        CountryEntity
    ).order_by(
        CountryEntity.countryName.desc()
    )
    result = await session.execute(sql)
    countries = result.scalars().all()
    return [
        CountryDomain(**{field: getattr(country, field) for field in CountryDomain.__fields__})
        for country in countries
    ]


async def genres_list(session: AsyncSession) -> list[GenreDomain]:
    sql = sa.select(GenreEntity)
    result = await session.execute(sql)
    genres = result.scalars().all()
    return [
        GenreDomain(**{field: getattr(genre, field) for field in GenreDomain.__fields__})
        for genre in genres
    ]


async def professions_list(session: AsyncSession) -> list[ProfessionDomain]:
    sql = sa.select(ProfessionEntity)
    result = await session.execute(sql)
    professions = result.scalars().all()
    return [
        ProfessionDomain(**{field: getattr(profession, field) for field in ProfessionDomain.__fields__})
        for profession in professions
    ]
