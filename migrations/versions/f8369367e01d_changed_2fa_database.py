"""Changed 2fa database

Revision ID: f8369367e01d
Revises: 16562ae5048b
Create Date: 2023-11-07 21:09:52.973934

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f8369367e01d'
down_revision = '16562ae5048b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_2fa_setup', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('is_2fa_setup')

    # ### end Alembic commands ###