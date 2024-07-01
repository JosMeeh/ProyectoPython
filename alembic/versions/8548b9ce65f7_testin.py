"""Testin

Revision ID: 8548b9ce65f7
Revises: 
Create Date: 2024-07-01 00:50:03.020908

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8548b9ce65f7'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Dish',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=True),
    sa.Column('description', sa.String(length=500), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Ingredient',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('amount', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Order',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('client_name', sa.String(length=30), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Users',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('name', sa.String(length=36), nullable=True),
    sa.Column('role', sa.String(length=36), nullable=True),
    sa.Column('token', sa.String(length=1024), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Users')
    op.drop_table('Order')
    op.drop_table('Ingredient')
    op.drop_table('Dish')
    # ### end Alembic commands ###
