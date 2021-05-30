"""empty message

Revision ID: 13e834d593f8
Revises: 20b1f27179d9
Create Date: 2021-05-30 00:52:43.644038

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '13e834d593f8'
down_revision = '20b1f27179d9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('movie', 'test')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('movie', sa.Column('test', sa.VARCHAR(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###