from pydantic import BaseModel


class PersonDomain(BaseModel):
    id: int
    photoUrl: str | None = None
    nameRu: str | None = None
    nameEn: str | None = None
