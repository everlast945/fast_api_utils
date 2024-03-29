"""create account table

Revision ID: 6896ac85e239
Revises:
Create Date: 2023-08-03 18:58:40.750444

"""
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from alembic import op

# revision identifiers, used by Alembic.
revision = '6896ac85e239'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'Country',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('countryName', sa.Text(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('countryName'),
    )
    op.create_table(
        'Genre',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('nameRu', sa.Text(), nullable=False),
        sa.Column('nameEn', sa.Text(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('nameRu'),
    )
    op.create_table(
        'Profession',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.Text(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('name'),
    )
    op.drop_index('ix_items_id', table_name='items')
    op.drop_index('ix_items_name', table_name='items')
    op.drop_table('items')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'items',
        sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column(
            'price',
            postgresql.DOUBLE_PRECISION(precision=53),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column(
            'tax',
            postgresql.DOUBLE_PRECISION(precision=53),
            autoincrement=False,
            nullable=False,
        ),
        sa.PrimaryKeyConstraint('id', name='items_pkey'),
    )
    op.create_index('ix_items_name', 'items', ['name'], unique=False)
    op.create_index('ix_items_id', 'items', ['id'], unique=False)
    op.drop_table('Profession')
    op.drop_table('Genre')
    op.drop_table('Country')
    # ### end Alembic commands ###
