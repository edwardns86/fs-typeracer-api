"""empty message

Revision ID: a9545a43d330
Revises: e9619366be15
Create Date: 2019-11-26 17:52:16.939573

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a9545a43d330'
down_revision = 'e9619366be15'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'scores', 'excerpts', ['excerpt_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'scores', type_='foreignkey')
    # ### end Alembic commands ###