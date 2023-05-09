from datetime import datetime

from pydantic import BaseModel

from internal.dictionaries.domain import CountryDomain, GenreDomain


class FilmDomain(BaseModel):
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
    persons: list[]