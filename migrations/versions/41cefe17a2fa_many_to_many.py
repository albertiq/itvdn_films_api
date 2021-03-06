"""many to many

Revision ID: 41cefe17a2fa
Revises: 3a4c539cd047
Create Date: 2021-12-15 22:25:34.460917

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '41cefe17a2fa'
down_revision = '3a4c539cd047'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('actors',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('birthday', sa.Date(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('movie_actors',
    sa.Column('actor_id', sa.Integer(), nullable=False),
    sa.Column('filmd_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['actor_id'], ['actors.id'], ),
    sa.ForeignKeyConstraint(['filmd_id'], ['films.id'], ),
    sa.PrimaryKeyConstraint('actor_id', 'filmd_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('movie_actors')
    op.drop_table('actors')
    # ### end Alembic commands ###
