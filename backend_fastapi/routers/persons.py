from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import get_session
from internal.persons.domain import PersonDomain, PersonDetailDomain
from internal.persons.services import PersonDetailService, persons_list


router = APIRouter(tags=["persons"])


@router.get("/persons/", summary='Список актеров/режиссеров')
async def persons_list_route(
        q: str = '',
        limit: int = 10,
        page: int = 1,
        session: AsyncSession = Depends(get_session),
) -> list[PersonDomain]:
    return await persons_list(q=q, limit=limit, page=page, session=session)


@router.get("/persons/{person_id}/", summary='Детальный просмотр актера/режиссера')
async def persons_detail_route(
    person_id: int,
    session: AsyncSession = Depends(get_session),
) -> PersonDetailDomain:
    return await PersonDetailService(session=session, person_id=person_id).run()
