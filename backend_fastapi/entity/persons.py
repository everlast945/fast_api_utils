import sqlalchemy as sa

from core.database import Base


class PersonEntity(Base):
    __tablename__ = 'Person'

    id = sa.Column(sa.Integer, primary_key=True)
    photoUrl = sa.Column(sa.Text)
    nameRu = sa.Column(sa.Text)
    nameEn = sa.Column(sa.Text)


t__PersonToProfession = sa.Table(
    '_PersonToProfession', Base.metadata,
    sa.Column('A', sa.ForeignKey('Person.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False),
    sa.Column('B', sa.ForeignKey('Profession.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True),
    sa.Index('_PersonToProfession_AB_unique', 'A', 'B', unique=True)
)
