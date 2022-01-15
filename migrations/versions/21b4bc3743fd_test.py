"""test

Revision ID: 21b4bc3743fd
Revises: 95b30a96dbec
Create Date: 2022-01-07 12:30:55.011301

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '21b4bc3743fd'
down_revision = '95b30a96dbec'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'zug', type_='foreignkey')
    op.create_foreign_key(None, 'zug', 'triebwagen', ['triebwagen'], ['fahrgestellnummer'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'zug', type_='foreignkey')
    op.create_foreign_key(None, 'zug', 'triebwagen', ['triebwagen'], ['fahrgestellnummer'])
    # ### end Alembic commands ###
