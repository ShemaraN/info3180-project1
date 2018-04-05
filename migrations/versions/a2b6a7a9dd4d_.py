"""empty message

Revision ID: a2b6a7a9dd4d
Revises: e232d7a75af6
Create Date: 2018-04-05 21:16:54.789404

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a2b6a7a9dd4d'
down_revision = 'e232d7a75af6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_profile', sa.Column('username', sa.String(length=80), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_profile', 'username')
    # ### end Alembic commands ###
