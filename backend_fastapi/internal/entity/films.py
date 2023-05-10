import sqlalchemy as sa
from core.database import Base


class FilmEntity(Base):
    __tablename__ = 'Film'

    id = sa.Column(sa.Integer, primary_key=True)
    trailerName = sa.Column(sa.Text)
    trailerUrl = sa.Column(sa.Text)
    ratingKp = sa.Column(sa.Float(53))
    votesKp = sa.Column(sa.Integer)
    ratingImdb = sa.Column(sa.Float(53))
    votesImdb = sa.Column(sa.Integer)
    ratingFilmCritics = sa.Column(sa.Float(53))
    votesFilmCritics = sa.Column(sa.Integer)
    ratingRussianFilmCritics = sa.Column(sa.Float(53))
    votesRussianFilmCritics = sa.Column(sa.Integer)
    movieLength = sa.Column(sa.Integer)
    originalFilmLanguage = sa.Column(sa.Text)
    filmNameRu = sa.Column(sa.Text, nullable=False)
    filmNameEn = sa.Column(sa.Text)
    description = sa.Column(sa.Text)
    premiereCountry = sa.Column(sa.Text)
    premiereWorldDate = sa.Column(sa.TIMESTAMP())
    slogan = sa.Column(sa.Text)
    bigPictureUrl = sa.Column(sa.Text)
    smallPictureUrl = sa.Column(sa.Text)
    year = sa.Column(sa.Integer)
    createdAt = sa.Column(sa.TIMESTAMP(), nullable=False)
    top10 = sa.Column(sa.Integer)
    top250 = sa.Column(sa.Integer)


class CommentEntity(Base):
    __tablename__ = 'Comment'

    id = sa.Column(sa.Integer, primary_key=True)
    header = sa.Column(sa.Text, nullable=False)
    value = sa.Column(sa.Text, nullable=False)
    filmId = sa.Column(
        sa.ForeignKey('Film.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False
    )
    authorId = sa.Column(sa.Integer, nullable=False)
    parentId = sa.Column(sa.Integer, nullable=False)
    createdAt = sa.Column(sa.TIMESTAMP(), nullable=False)


class FactEntity(Base):
    __tablename__ = 'Fact'

    id = sa.Column(sa.Integer, primary_key=True)
    value = sa.Column(sa.Text, nullable=False)
    type = sa.Column(sa.Text, nullable=False)
    spoiler = sa.Column(sa.Boolean, nullable=False)
    filmId = sa.Column(
        sa.ForeignKey('Film.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False
    )


t__CountryToFilm = sa.Table(
    '_CountryToFilm',
    Base.metadata,
    sa.Column(
        'A',
        sa.ForeignKey('Country.id', ondelete='CASCADE', onupdate='CASCADE'),
        nullable=False,
    ),
    sa.Column(
        'B',
        sa.ForeignKey('Film.id', ondelete='CASCADE', onupdate='CASCADE'),
        nullable=False,
        index=True,
    ),
    sa.Index('_CountryToFilm_AB_unique', 'A', 'B', unique=True),
)


t__FilmToGenre = sa.Table(
    '_FilmToGenre',
    Base.metadata,
    sa.Column(
        'A',
        sa.ForeignKey('Film.id', ondelete='CASCADE', onupdate='CASCADE'),
        nullable=False,
    ),
    sa.Column(
        'B',
        sa.ForeignKey('Genre.id', ondelete='CASCADE', onupdate='CASCADE'),
        nullable=False,
        index=True,
    ),
    sa.Index('_FilmToGenre_AB_unique', 'A', 'B', unique=True),
)


t__FilmToPerson = sa.Table(
    '_FilmToPerson',
    Base.metadata,
    sa.Column(
        'A',
        sa.ForeignKey('Film.id', ondelete='CASCADE', onupdate='CASCADE'),
        nullable=False,
    ),
    sa.Column(
        'B',
        sa.ForeignKey('Person.id', ondelete='CASCADE', onupdate='CASCADE'),
        nullable=False,
        index=True,
    ),
    sa.Index('_FilmToPerson_AB_unique', 'A', 'B', unique=True),
)
