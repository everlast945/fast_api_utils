from pydantic import BaseModel


class GenreDomain(BaseModel):
    id: int
    nameRu: str
    nameEn: str
