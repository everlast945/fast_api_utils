from pydantic import BaseModel


class PersonFilmDomain(BaseModel):
    id: int


class PersonProfession(BaseModel):
    id: int
    name: str


class PersonDetailDomain(BaseModel):
    id: int
    photoUrl: str | None = None
    nameRu: str | None = None
    nameEn: str | None = None
    films: list[PersonFilmDomain]
    professions: list[PersonProfession]
