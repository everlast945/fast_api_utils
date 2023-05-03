from pydantic import BaseModel


class ItemDomain(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
