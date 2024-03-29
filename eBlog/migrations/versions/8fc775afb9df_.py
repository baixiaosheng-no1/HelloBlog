"""empty message

Revision ID: 8fc775afb9df
Revises: ec1bc405b3de
Create Date: 2019-06-29 18:39:54.923418

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '8fc775afb9df'
down_revision = 'ec1bc405b3de'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('art_moel', sa.Column('values', sa.Text(), nullable=True))
    op.drop_column('art_moel', 'content')
    op.drop_column('art_moel', 'date')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('art_moel', sa.Column('date', sa.DATE(), nullable=True))
    op.add_column('art_moel', sa.Column('content', mysql.TEXT(), nullable=True))
    op.drop_column('art_moel', 'values')
    # ### end Alembic commands ###
