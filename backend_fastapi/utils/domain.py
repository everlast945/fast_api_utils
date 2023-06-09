from typing import Type

from core.database import Base
from pydantic import BaseModel


def map_fields(entity: Base, domain_class: Type[BaseModel]) -> dict:
    return {
        field: getattr(entity, field)
        for field in domain_class.__fields__
        if hasattr(entity, field)
    }
