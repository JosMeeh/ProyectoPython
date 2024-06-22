"""Create users table

Revision ID: 748fab4fef13
Revises: 
Create Date: 2024-06-22 17:35:32.805696

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '748fab4fef13'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
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
    # ### end Alembic commands ###
