"""train names

Revision ID: 18a5c914c33e
Revises: 301a53f79ca6
Create Date: 2021-11-21 13:09:16.497411

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '18a5c914c33e'
down_revision = '301a53f79ca6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('zug', sa.Column('name', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('zug', 'name')
    # ### end Alembic commands ###