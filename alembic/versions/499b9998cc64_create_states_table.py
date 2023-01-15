"""create states table

Revision ID: 499b9998cc64
Revises: 
Create Date: 2023-01-14 13:15:39.914077

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '499b9998cc64'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'states',
        sa.Column('name', sa.String(255), primary_key=True),
        sa.Column('created_at', sa.DateTime, nullable=False,
                  server_default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime, nullable=False,
                  server_default=sa.func.now(), onupdate=sa.func.now())

    )


def downgrade():
    op.drop_table('states')
