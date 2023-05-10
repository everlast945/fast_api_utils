from core.database import get_session
from fastapi import APIRouter, Depends
from internal.apps.dictionaries.domain import (
    CountryDomain,
    GenreDomain,
    ProfessionDomain,
)
from internal.apps.dictionaries.services import (
    country_list,
    genres_list,
    professions_list,
)
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(tags=["dictionaries"])


@router.get("/dictionaries/countries/", summary='Справочник стран')
async def dictionaries_countries(
    session: AsyncSession = Depends(get_session),
) -> list[CountryDomain]:
    return await country_list(session)


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
