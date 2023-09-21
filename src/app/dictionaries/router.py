from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.clickhouse_test.service import country_clickhouse_list
from app.dictionaries.schemas.country import CountryDomain
from app.dictionaries.schemas.genre import GenreDomain
from app.dictionaries.schemas.profession import ProfessionDomain
from app.dictionaries.services.country_list import country_detail, country_list
from app.dictionaries.services.genres_list import genres_list
from app.dictionaries.services.professions_list import professions_list
from core.clickhouse import get_clickhouse_session
from core.database import get_session

router = APIRouter(tags=["dictionaries"])


@router.get("/dictionaries/countries/", summary='Справочник стран')
async def dictionaries_countries(
    session: AsyncSession = Depends(get_session),
) -> list[CountryDomain]:
    return await country_list(session)


@router.get("/dictionaries/countries/<pk>/", summary='Справочник стран')
async def dictionaries_detail(
    pk: int,
    session: AsyncSession = Depends(get_session),
) -> CountryDomain:
    return await country_detail(session, pk)


@router.get("/dictionaries/clickhouse/countries/", summary='Справочник стран')
async def dictionaries_clickhouse_countries(
    session: AsyncSession = Depends(get_clickhouse_session),
) -> list[CountryDomain]:
    return await country_clickhouse_list(session)


@router.get("/dictionaries/genres/", summary='Справочник жанров')
async def dictionaries_genres(
    session: AsyncSession = Depends(get_session),
) -> list[GenreDomain]:
    return await genres_list(session)


@router.get("/dictionaries/professions/", summary='Справочник профессий')
async def dictionaries_professions(
    session: AsyncSession = Depends(get_session),
) -> list[ProfessionDomain]:
    return await professions_list(session)
