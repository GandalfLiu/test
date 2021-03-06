"""empty message

Revision ID: 4726d47c0118
Revises: 
Create Date: 2018-10-19 09:20:38.023194

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4726d47c0118'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('wheel',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('imgPath', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('wheel')
    # ### end Alembic commands ###
