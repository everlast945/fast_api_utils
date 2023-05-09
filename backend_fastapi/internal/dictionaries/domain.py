from pydantic import BaseModel


class CountryDomain(BaseModel):
    id: int
    countryName: str


class GenreDomain(BaseModel):
    id: int
    nameRu: str
    nameEn: str


class ProfessionDomain(BaseModel):
    id: int
    name: str
