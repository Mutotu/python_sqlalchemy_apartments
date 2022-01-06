"""create_aparment_model

Revision ID: 183339632820
Revises: 
Create Date: 2022-01-05 09:46:43.383558

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '183339632820'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'apartments',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String, nullable=False, unique=True),
        sa.Column('units', sa.Integer,),
        sa.Column("owner_id", sa.String)
        
    )


def downgrade():
    pass
