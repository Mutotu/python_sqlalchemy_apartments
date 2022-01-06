"""create_owner_model

Revision ID: 78493af1b4eb
Revises: 183339632820
Create Date: 2022-01-05 09:52:53.594441

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '78493af1b4eb'
down_revision = '183339632820'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'owners',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String, nullable=False,),
        sa.Column('age', sa.Integer)
    )


def downgrade():
    pass
