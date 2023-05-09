import sqlalchemy as sa

from core.database import Base

class CountryEntity(Base):
    __tablename__ = 'Country'

    id = sa.Column(sa.Integer, primary_key=True)
    countryName = sa.Column(sa.Text, nullable=False, unique=True)

class GenreEntity(Base):
    __tablename__ = 'Genre'

    id = sa.Column(sa.Integer, primary_key=True)
    nameRu = sa.Column(sa.Text, nullable=False, unique=True)
    nameEn = sa.Column(sa.Text)

class ProfessionEntity(Base):
    __tablename__ = 'Profession'

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.Text, nullable=False, unique=True)
