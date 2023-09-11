from pydantic import BaseModel


class ProfessionDomain(BaseModel):
    id: int
    name: str
