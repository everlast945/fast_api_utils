import uuid

import clickhouse_sqlalchemy as csa
import clickhouse_sqlalchemy.types
import sqlalchemy as sa

from core.clickhouse import Base


class LegAvailabilityHistory(Base):
    __tablename__ = 'LegAvailabilityHistory'
    uid = sa.Column(
        csa.types.UUID, primary_key=True, default=lambda _: str(uuid.uuid4())
    )
    legId = sa.Column(csa.types.UUID)
    available = sa.Column(csa.types.Int)
    booked = sa.Column(csa.types.Int)
    waitlist = sa.Column(csa.types.Int)
    state = sa.Column(csa.types.String)
    updated = sa.Column(csa.types.DateTime)


class CabinAvailabilityHistory(Base):
    __tablename__ = 'CabinAvailabilityHistory'
    uid = sa.Column(
        csa.types.UUID, primary_key=True, default=lambda _: str(uuid.uuid4())
    )
    LegAvailabilityId = sa.Column(
        csa.types.UUID, sa.ForeignKey('LegAvailabilityHistory.uid')
    )
    code = sa.Column(csa.types.String)
    available = sa.Column(csa.types.Int)
    booked = sa.Column(csa.types.Int)
    waitlist = sa.Column(csa.types.Int)


class SubclassAvailabilityHistory(Base):
    __tablename__ = 'SubclassAvailabilityHistory'
    uid = sa.Column(
        csa.types.UUID, primary_key=True, default=lambda _: str(uuid.uuid4())
    )
    CabinAvailabilityId = sa.Column(
        csa.types.UUID, sa.ForeignKey('CabinAvailabilityHistory.uid')
    )
    state = sa.Column(csa.types.String)
    code = sa.Column(csa.types.String)
    available = sa.Column(csa.types.Int)
    booked = sa.Column(csa.types.Int)
    waitlist = sa.Column(csa.types.Int)
