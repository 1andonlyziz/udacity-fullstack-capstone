"""empty message

Revision ID: 20b1f27179d9
Revises: 
Create Date: 2021-05-30 00:51:29.410706

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '20b1f27179d9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('movie', sa.Column('test', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('movie', 'test')
    # ### end Alembic commands ###
