"""Add page abstract

Revision ID: 27af318320bd
Revises: None
Create Date: 2014-02-27 19:33:58.700529

"""

# revision identifiers, used by Alembic.
revision = '27af318320bd'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('page', sa.Column('abstract', sa.Unicode(length=255),
                                    nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('page', 'abstract')
    ### end Alembic commands ###
