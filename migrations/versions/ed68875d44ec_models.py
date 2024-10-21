"""models

Revision ID: ed68875d44ec
Revises: 
Create Date: 2024-10-18 12:45:55.495765

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlalchemy.dialects.postgresql as psql

from api.game_handler import GameStatus, GamePlayerRole, GameColor, CardStatus


# revision identifiers, used by Alembic.
revision: str = 'ed68875d44ec'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('user_id', sa.Integer, primary_key=True),
        sa.Column('username', sa.Text, nullable=False),
        sa.Column('password_hash', sa.Text, nullable=False),
        sa.Column('created_at', sa.TIMESTAMP, nullable=False)
    )

    op.execute(
        "CREATE TYPE game_status AS ENUM ('INIT', 'CREATED', 'STARTED', 'FINISHED');"
    )

    op.create_table(
        'games',
        sa.Column('game_id', sa.Integer, primary_key=True),
        sa.Column('created_by', sa.Integer, sa.ForeignKey('users.user_id')),
        sa.Column('created_at', sa.TIMESTAMP, nullable=False),
        sa.Column('status', psql.ENUM( GameStatus, name='game_status', create_type=False), nullable=False)
    )

    op.create_table(
        'rooms',
        sa.Column('room_id', sa.Integer, primary_key=True),
        sa.Column('game_id', sa.Integer, sa.ForeignKey('games.game_id')),
        sa.Column('max_players', sa.Integer, nullable=False),
        sa.Column('created_at', sa.TIMESTAMP, nullable=False)
    )

    op.execute(
        "CREATE TYPE player_role AS ENUM ('CAPTAIN', 'PLAYER');"
    )

    op.execute(
        "CREATE TYPE player_team AS ENUM ('WHITE', 'BLACK', 'RED', 'BLUE')"
    )

    op.create_table(
        'game_players',
        sa.Column('game_id', sa.Integer, sa.ForeignKey('games.game_id'), primary_key=True),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('users.user_id'), primary_key=True),
        sa.Column('role', psql.ENUM(GamePlayerRole, name='player_role', create_type=False), nullable=False),
        sa.Column('team', psql.ENUM(GameColor, name='player_team', create_type=False), nullable=False),
        sa.Column('joined_at', sa.TIMESTAMP, nullable=False)
    )

    op.create_table(
        'images',
        sa.Column('image_id', sa.Integer, primary_key=True),
        sa.Column('url', sa.Text, nullable=False),
        sa.Column('generated_for_game', sa.Integer, sa.ForeignKey('games.game_id')),
        sa.Column('description', sa.Text, nullable=True),
        sa.Column('created_at', sa.TIMESTAMP, nullable=False)
    )

    op.execute(
        "CREATE TYPE card_team AS ENUM ('WHITE', 'BLACK', 'RED', 'BLUE');"
    )

    op.execute(
        "CREATE TYPE card_status AS ENUM ('NOT_CLICKED', 'CLICKED');"
    )

    op.create_table(
        'cards',
        sa.Column('card_id', sa.Integer, primary_key=True),
        sa.Column('game_id', sa.Integer, sa.ForeignKey('games.game_id')),
        sa.Column('image_id', sa.Integer, sa.ForeignKey('images.image_id')),
        sa.Column('team', psql.ENUM(GameColor, name='card_team', create_type=False), nullable=False),
        sa.Column('status', psql.ENUM(CardStatus, name='card_status', create_type=False), nullable=False)
    )


    op.create_table(
        'clues',
        sa.Column('clue_id', sa.Integer, primary_key=True),
        sa.Column('game_id', sa.Integer, sa.ForeignKey('games.game_id')),
        sa.Column('given_by', sa.Integer, sa.ForeignKey('users.user_id')),
        sa.Column('clue_text', sa.Text, nullable=False),
        sa.Column('created_at', sa.TIMESTAMP, nullable=False)
    )

    op.create_table(
        'moves',
        sa.Column('move_id', sa.Integer, primary_key=True),
        sa.Column('game_id', sa.Integer, sa.ForeignKey('games.game_id')),
        sa.Column('card_id', sa.Integer, sa.ForeignKey('cards.card_id')),
        sa.Column('chosen_by', sa.Integer, sa.ForeignKey('users.user_id')),
        sa.Column('created_at', sa.TIMESTAMP, nullable=False)
    )


def downgrade() -> None:
    op.drop_table('users')
    op.execute('DROP TYPE game_status')
    op.drop_table('games')
    op.drop_table('rooms')
    op.execute('DROP TYPE player_role')
    op.execute('DROP TYPE player_team')
    op.drop_table('game_players')
    op.drop_table('images')
    op.execute('DROP TYPE card_team')
    op.execute('DROP TYPE card_status')
    op.drop_table('cards')
    op.drop_table('clues')
    op.drop_table('moves')
