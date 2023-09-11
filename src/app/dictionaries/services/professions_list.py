import sqlalchemy as sa
from sqlalchemy.ext.asyncio import AsyncSession

from app.dictionaries.models import ProfessionEntity
from app.dictionaries.schemas.profession import ProfessionDomain


async def professions_list(session: AsyncSession) -> list[ProfessionDomain]:
    sql = sa.select(ProfessionEntity)
    result = await session.execute(sql)
    professions = result.scalars().all()
    return [
        ProfessionDomain(
            **{
                field: getattr(profession, field)
                for field in ProfessionDomain.__fields__
            }
        )
        for profession in professions
    ]
