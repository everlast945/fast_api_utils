from datetime import datetime

from internal.apps.dictionaries.domain import CountryDomain, GenreDomain
from internal.apps.persons.domain.person import PersonDomain
from pydantic import BaseModel


class FilmDetailDomain(BaseModel):
    id: int
    trailerName: str | None = None
    trailerUrl: str | None = None
    originalFilmLanguage: str | None = None
    filmNameRu: str | None = None
    filmNameEn: str | None = None
    description: str | None = None
    premiereCountry: str | None = None
    slogan: str | None = None
    bigPictureUrl: str | None = None
    smallPictureUrl: str | None = None
    ratingKp: float | None = None
    ratingImdb: float | None = None
    ratingFilmCritics: float | None = None
    ratingRussianFilmCritics: float | None = None
    year: int | None = None
    movieLength: int | None = None
    votesKp: int | None = None
    votesImdb: int | None = None
    votesRussianFilmCritics: int | None = None
    votesFilmCritics: int | None = None
    top10: int | None = None
    top250: int | None = None
    premiereWorldDate: datetime | None = None
    createdAt: datetime | None = None
    countries: list[CountryDomain]
    genries: list[GenreDomain]
    persons: list[PersonDomain]
