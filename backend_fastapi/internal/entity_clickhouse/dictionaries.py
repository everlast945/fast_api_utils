import sqlalchemy as sa
from clickhouse_sqlalchemy import engines
from core.clickhouse import Base


class CountryEntity(Base):
    __tablename__ = 'Country'

    id = sa.Column(sa.Integer, primary_key=True)
    countryName = sa.Column(sa.Text)

    __table_args__ = (engines.Memory(),)


class GenreEntity(Base):
    __tablename__ = 'Genre'

    id = sa.Column(sa.Integer, primary_key=True)
    nameRu = sa.Column(sa.Text)
    nameEn = sa.Column(sa.Text)

    __table_args__ = (engines.Memory(),)


class ProfessionEntity(Base):
    __tablename__ = 'Profession'

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.Text)

    __table_args__ = (engines.Memory(),)
