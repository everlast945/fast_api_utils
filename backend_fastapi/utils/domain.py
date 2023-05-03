from pydantic import BaseModel


class BaseListDomain(BaseModel):
    q: str = ''
    sort: list[str] | None = None
    page: int = 1
    limit: int = 10
