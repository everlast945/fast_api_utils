import sqlalchemy as sa
from core.database import Base


class ItemEntity(Base):
    __tablename__ = "items"

    id = sa.Column(sa.Integer, primary_key=True, index=True)
    name = sa.Column(sa.String, unique=True, index=True)
    description = sa.Column(sa.String, nullable=False, default='')
    price = sa.Column(sa.Float, nullable=False, default=0)
    tax = sa.Column(sa.Float, nullable=False, default=0)


