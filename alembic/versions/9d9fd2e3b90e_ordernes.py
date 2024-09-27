"""Ordernes

Revision ID: 9d9fd2e3b90e
Revises: 
Create Date: 2024-07-03 11:50:31.092960

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9d9fd2e3b90e'
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
    sa.Column('instructions', sa.String(length=1000), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Ingredient',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('amount', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Menu',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=True),
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
    op.create_table('Menu_Dishes',
    sa.Column('id_Dish', sa.UUID(), nullable=False),
    sa.Column('id_Menu', sa.UUID(), nullable=False),
    sa.ForeignKeyConstraint(['id_Dish'], ['Dish.id'], ),
    sa.ForeignKeyConstraint(['id_Menu'], ['Menu.id'], ),
    sa.PrimaryKeyConstraint('id_Dish', 'id_Menu')
    )
    op.create_table('Order_Dishes',
    sa.Column('id_Order', sa.UUID(), nullable=False),
    sa.Column('id_Dish', sa.UUID(), nullable=False),
    sa.Column('amount', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_Dish'], ['Dish.id'], ),
    sa.ForeignKeyConstraint(['id_Order'], ['Order.id'], ),
    sa.PrimaryKeyConstraint('id_Order', 'id_Dish')
    )
    op.create_table('Recipe_Ingredient',
    sa.Column('id_Dish', sa.UUID(), nullable=False),
    sa.Column('id_Ingredient', sa.UUID(), nullable=False),
    sa.Column('amount', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_Dish'], ['Dish.id'], ),
    sa.ForeignKeyConstraint(['id_Ingredient'], ['Ingredient.id'], ),
    sa.PrimaryKeyConstraint('id_Dish', 'id_Ingredient')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Recipe_Ingredient')
    op.drop_table('Order_Dishes')
    op.drop_table('Menu_Dishes')
    op.drop_table('Users')
    op.drop_table('Order')
    op.drop_table('Menu')
    op.drop_table('Ingredient')
    op.drop_table('Dish')
    # ### end Alembic commands ###