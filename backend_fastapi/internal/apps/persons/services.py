import sqlalchemy as sa
from internal.apps.persons.domain.person import PersonDomain
from internal.apps.persons.domain.person_detail import (
    PersonDetailDomain,
    PersonFilmDomain,
    PersonProfession,
)
from internal.entity.dictionaries import ProfessionEntity
from internal.entity.films import FilmEntity, t__FilmToPerson
from internal.entity.persons import PersonEntity, t__PersonToProfession
from sqlalchemy.ext.asyncio import AsyncSession


class PersonDetailService:
    def __init__(self, session: AsyncSession, person_id: int) -> None:
        super().__init__()
        self.session = session
        self.person_id = person_id

    async def run(self) -> PersonDetailDomain:
        person: PersonEntity = await self._get_person()
        films: list[FilmEntity] = await self._get_films()
        professions: list[ProfessionEntity] = await self._get_professions()
        return PersonDetailDomain(
            id=person.id,
            photoUrl=person.photoUrl,
            nameRu=person.nameRu,
            nameEn=person.nameEn,
            films=await self._serialize_films(films),
            professions=await self._serialize_professions(professions),
        )

    async def _get_person(self) -> PersonEntity:
        sql = sa.select(PersonEntity).where(
            PersonEntity.id == self.person_id,
        )
        result = await self.session.execute(sql)
        return result.scalars().first()

    async def _get_films(self) -> list[FilmEntity]:
        sql = (
            sa.select(FilmEntity)
            .outerjoin(t__FilmToPerson, t__FilmToPerson.c.A == FilmEntity.id)
            .outerjoin(PersonEntity, PersonEntity.id == t__FilmToPerson.c.B)
            .where(
                PersonEntity.id == self.person_id,
            )
        )
        result = await self.session.execute(sql)
        return result.scalars().all()

    async def _get_professions(self) -> list[ProfessionEntity]:
        sql = (
            sa.select(ProfessionEntity)
            .join(
                t__PersonToProfession, t__PersonToProfession.c.B == ProfessionEntity.id
            )
            .join(PersonEntity, PersonEntity.id == t__PersonToProfession.c.A)
            .where(PersonEntity.id == self.person_id)
        )
        result = await self.session.execute(sql)
        return result.scalars().all()

    async def _serialize_films(self, films: list[FilmEntity]):
        return [
            PersonFilmDomain(
                id=film.id,
            )
            for film in films
        ]

    async def _serialize_professions(
        self, professions: list[ProfessionEntity]
    ) -> list[PersonProfession]:
        return [
            PersonProfession(
                id=profession.id,
                name=profession.name,
            )
            for profession in professions
        ]


async def persons_list(
    session: AsyncSession,
    q: str = '',
    limit: int = 10,
    page: int = 1,
):
    offset = (page - 1) * limit if page else 0
    sql = sa.select(PersonEntity).limit(limit).offset(offset)
    if q:
        sql = sql.where(
            sa.or_(
                PersonEntity.nameEn.ilike(f'{q}%'),
                PersonEntity.nameRu.ilike(f'{q}%'),
                PersonEntity.nameEn.ilike(f'% {q}%'),
                PersonEntity.nameRu.ilike(f'% {q}%'),
            ),
        )
    result = await session.execute(sql)
    persons = result.scalars().all()
    return [
        PersonDomain(
            **{field: getattr(person, field) for field in PersonDomain.__fields__}
        )
        for person in persons
    ]
