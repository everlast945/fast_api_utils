import sqlalchemy as sa
from sqlalchemy.ext.asyncio import AsyncSession

from app.dictionaries.models import GenreEntity
from app.dictionaries.schemas.genre import GenreDomain


async def genres_list(session: AsyncSession) -> list[GenreDomain]:
    sql = sa.select(GenreEntity)
    result = await session.execute(sql)
    genres = result.scalars().all()
    return [
        GenreDomain(
            **{field: getattr(genre, field) for field in GenreDomain.__fields__}
        )
        for genre in genres
    ]
