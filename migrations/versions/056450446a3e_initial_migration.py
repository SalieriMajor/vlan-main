"""Initial migration

Revision ID: 056450446a3e
Revises: 
Create Date: 2020-12-08 08:12:43.215913

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '056450446a3e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('vlans',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('state', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vlans')
    # ### end Alembic commands ###