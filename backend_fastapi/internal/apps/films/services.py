import sqlalchemy as sa
from sqlalchemy.ext.asyncio import AsyncSession

from internal.entity.dictionaries import CountryEntity, GenreEntity
from internal.entity.films import FilmEntity, t__CountryToFilm, t__FilmToGenre, t__FilmToPerson
from internal.entity.persons import PersonEntity
from internal.apps.dictionaries.domain import CountryDomain, GenreDomain
from internal.apps.films.domain.film import FilmDomain
from internal.apps.films.domain.film_detail import FilmDetailDomain
from internal.apps.persons.domain.person import PersonDomain
from utils.domain import map_fields


class FilmDetailService:

    def __init__(self, session: AsyncSession, film_id: int) -> None:
        super().__init__()
        self.session = session
        self.film_id = film_id

    async def get_film_detail(self) -> FilmDetailDomain:
        film = await self._get_film()
        return FilmDetailDomain(
            **map_fields(film, FilmDetailDomain),
            countries=await self._get_countries(),
            genries=await self._get_genres(),
            persons=await self._get_persons(),
        )

    async def _get_film(self) -> FilmEntity:
        sql = sa.select(FilmEntity).where(
            FilmEntity.id == self.film_id
        )
        result = await self.session.execute(sql)
        return result.scalars().first()

    async def _get_countries(self):
        sql = sa.select(CountryEntity).join(
            t__CountryToFilm, t__CountryToFilm.c.A == CountryEntity.id
        ).join(
            FilmEntity, FilmEntity.id == t__CountryToFilm.c.B
        ).where(
            FilmEntity.id == self.film_id
        )
        result = await self.session.execute(sql)
        countries = result.scalars().all()
        return [
            CountryDomain(**map_fields(country, CountryDomain)) for country in countries
        ]

    async def _get_genres(self):
        sql = sa.select(GenreEntity).join(
            t__FilmToGenre, t__FilmToGenre.c.B == GenreEntity.id
        ).join(
            FilmEntity, FilmEntity.id == t__FilmToGenre.c.A
        ).where(
            FilmEntity.id == self.film_id
        )
        result = await self.session.execute(sql)
        items = result.scalars().all()
        return [
            GenreDomain(**map_fields(item, GenreDomain)) for item in items
        ]

    async def _get_persons(self):
        sql =sa.select(PersonEntity).join(
            t__FilmToPerson, t__FilmToPerson.c.B == PersonEntity.id
        ).join(
            FilmEntity, FilmEntity.id == t__FilmToPerson.c.A
        ).where(
            FilmEntity.id == self.film_id
        )
        result = await self.session.execute(sql)
        items = result.scalars().all()
        return [
            PersonDomain(**map_fields(item, PersonDomain)) for item in items
        ]


async def films_list(
    session: AsyncSession,
    q: str = '',
    limit: int = 10,
    page: int = 1,
) -> list[FilmDomain]:
    offset = (page - 1) * limit if page else 0
    sql = sa.select(FilmEntity).limit(limit).offset(offset)
    if q:
        sql = sql.where(
            sa.or_(
                FilmEntity.filmNameEn.ilike(f'{q}%'),
                FilmEntity.filmNameRu.ilike(f'{q}%'),
                FilmEntity.filmNameEn.ilike(f'% {q}%'),
                FilmEntity.filmNameRu.ilike(f'% {q}%'),
            ),
        )
    result = await session.execute(sql)
    items = result.scalars().all()
    return [
        FilmDomain(**{field: getattr(item, field) for field in FilmDomain.__fields__})
        for item in items
    ]
