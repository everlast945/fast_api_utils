from pydantic import BaseModel


class CountryDomain(BaseModel):
    id: int
    countryName: str
