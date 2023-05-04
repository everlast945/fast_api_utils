from pydantic import BaseModel


class ItemDomain(BaseModel):
    id: int | None = None
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
