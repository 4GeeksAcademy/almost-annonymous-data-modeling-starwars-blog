"""empty message

Revision ID: 6fdb2d5914f7
Revises: 01b52073ffd8
Create Date: 2025-06-13 23:56:58.662749

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6fdb2d5914f7'
down_revision = '01b52073ffd8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('favorite_characters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('character_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['character_id'], ['character.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_id'),
    sa.UniqueConstraint('user_id', 'character_id', name='no_duplicate_for_user_and_character')
    )
    op.create_table('favorite_planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('planet_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['planet_id'], ['planet.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_id'),
    sa.UniqueConstraint('user_id', 'planet_id', name='no_duplicate_for_user_and_planet')
    )
    op.create_table('favorite_vehicles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('vehicle_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['vehicle_id'], ['vehicle.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_id'),
    sa.UniqueConstraint('user_id', 'vehicle_id', name='no_duplicate_for_user_and_vehicle')
    )
    op.drop_table('favorite')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('favorite',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('character_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('planet_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('vehicle_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['character_id'], ['character.id'], name='favorite_character_id_fkey'),
    sa.ForeignKeyConstraint(['planet_id'], ['planet.id'], name='favorite_planet_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='favorite_user_id_fkey'),
    sa.ForeignKeyConstraint(['vehicle_id'], ['vehicle.id'], name='favorite_vehicle_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='favorite_pkey'),
    sa.UniqueConstraint('user_id', name='favorite_user_id_key')
    )
    op.drop_table('favorite_vehicles')
    op.drop_table('favorite_planets')
    op.drop_table('favorite_characters')
    # ### end Alembic commands ###
