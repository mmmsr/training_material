"""empty message

Revision ID: 01fae71fbee8
Revises: fc00821f3ea4
Create Date: 2019-05-01 15:53:39.538853

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '01fae71fbee8'
down_revision = 'fc00821f3ea4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('entries',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('body', sa.String(), nullable=False),
    sa.Column('posted_by', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('entries')
    # ### end Alembic commands ###
