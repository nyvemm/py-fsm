"""create transitions table

Revision ID: b2157dfd39fe
Revises: 499b9998cc64
Create Date: 2023-01-14 13:19:40.722088

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b2157dfd39fe'
down_revision = '499b9998cc64'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('transitions',
                    sa.Column('name', sa.String(255), primary_key=True),
                    sa.Column('from_state', sa.String(255), nullable=False),
                    sa.Column('to_state', sa.String(255), nullable=False),
                    sa.Column('created_at', sa.DateTime(), nullable=False,
                              server_default=sa.func.now()),
                    sa.Column('updated_at', sa.DateTime(), nullable=False,
                              server_default=sa.func.now(), onupdate=sa.func.now()),
                    sa.PrimaryKeyConstraint('name'),
                    sa.ForeignKeyConstraint(['from_state'], ['states.name'], ),
                    sa.ForeignKeyConstraint(['to_state'], ['states.name'], )
                    )


def downgrade() -> None:
    op.create_table('states',
                    sa.Column('name', sa.INTEGER(),
                              autoincrement=True, nullable=False),
                    sa.Column('name', sa.VARCHAR(length=255),
                              autoincrement=False, nullable=False),
                    sa.PrimaryKeyConstraint('name', name='states_pkey')
                    )
    op.drop_table('transitions')
