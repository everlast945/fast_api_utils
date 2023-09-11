from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.clickhouse_test import service as clickhouse_service
from app.dictionaries.schemas.country import CountryDomain
from core.database import get_session

router = APIRouter(tags=["clickhouse"])


@router.get("/clickhouse/dictionaries/countries/", summary='Справочник стран')
async def dictionaries_countries(
    session: AsyncSession = Depends(get_session),
) -> list[CountryDomain]:
    return await clickhouse_service.country_clickhouse_list(session)
