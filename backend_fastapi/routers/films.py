from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import get_session
from internal.films.domain import FilmDetailDomain, FilmDomain
from internal.films.services import FilmDetailService, films_list

router = APIRouter(tags=["films"])


@router.get("/films/", summary='Список Item')
async def films_list_route(
    q: str = '',
    limit: int = 10,
    page: int = 1,
    session: AsyncSession = Depends(get_session),
) -> list[FilmDomain]:
    return await films_list(q=q, limit=limit, page=page, session=session)


@router.get("/films/{film_id}", summary='Список Item')
async def films_detail_route(film_id: int, session: AsyncSession = Depends(get_session)) -> FilmDetailDomain:
    return await FilmDetailService(session=session, film_id=film_id).get_film_detail()
