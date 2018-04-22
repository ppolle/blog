"""added image column to post table

Revision ID: d4b9ae91a836
Revises: b1c60c6ffc65
Create Date: 2018-04-22 15:22:43.470960

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd4b9ae91a836'
down_revision = 'b1c60c6ffc65'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('image', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'image')
    # ### end Alembic commands ###