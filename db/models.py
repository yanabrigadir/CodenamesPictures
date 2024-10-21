from sqlalchemy import Column, Enum
from sqlalchemy import String, Text, Integer, TIMESTAMP, VARCHAR, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

from api.game_handler import GameStatus, GamePlayerRole, GameColor, CardStatus

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    username = Column(Text, nullable=False)
    password_hash = Column(Text, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False)

    games = relationship('Game', back_populates='creator')
    game_players = relationship('GamePlayer', back_populates='user')
    clue = relationship('Clue', back_populates='user')
    move = relationship('Move', back_populates='user')


class Game(Base):
    __tablename__ = 'games'

    game_id = Column(Integer, primary_key=True)
    created_by = Column(Integer, ForeignKey('users.user_id'))
    created_at = Column(TIMESTAMP, nullable=False)
    status = Column(Enum(GameStatus, name='game_status', create_type=False), nullable=False)

    creator = relationship('User', back_populates='games')
    rooms = relationship('Room', back_populates='game')
    game_players = relationship('GamePlayer', back_populates='game')
    image = relationship('Image', back_populates='game')
    card = relationship('Card', back_populates='game')
    clue = relationship('Clue', back_populates='game')
    move = relationship('Move', back_populates='game')


class Room(Base):
    __tablename__ = 'rooms'

    room_id = Column(Integer, primary_key=True)
    game_id = Column(Integer, ForeignKey('games.game_id'))
    max_players = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False)

    game = relationship('Game', back_populates='rooms')



class GamePlayer(Base):
    __tablename__ = 'game_players'

    game_id = Column(Integer, ForeignKey('games.game_id'), primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), primary_key=True)
    role = Column(Enum(GamePlayerRole, name='player_role', create_type=False), nullable=False)
    team = Column(Enum(GameColor, name='player_team', create_type=False), nullable=False)
    joined_at = Column(TIMESTAMP, nullable=False)

    game = relationship('Game', back_populates='game_players')
    user = relationship('User', backref='game_players')


class Image(Base):
    __tablename__ = 'images'

    image_id = Column(Integer, primary_key=True)
    url = Column(Text, nullable=False)
    generated_for_game = Column(Integer, ForeignKey('games.game_id'))
    description = Column(Text, nullable=True)
    created_at = Column(TIMESTAMP, nullable=False)

    game = relationship('Game', back_populates='image')
    card = relationship('Card', uselist=False)


class Card(Base):
    __tablename__ = 'cards'

    card_id = Column(Integer, primary_key=True)
    game_id = Column(Integer, ForeignKey('games.games_id'))
    image_id = Column(Integer, ForeignKey('images.image_id'))
    team = Column(Enum(GameColor, name='card_team', create_type=False), nullable=False)
    status = Column(Enum(CardStatus, name='card_status', create_type=False), nullable=False)

    game = relationship('Game', back_populates='card')
    image = relationship('Image', uselist=False)
    move = relationship('Move', back_populates='card')


class Clue(Base):
    __tablename__ = 'clues'

    clue_id = Column(Integer, primary_key=True)
    game_id = Column(Integer, ForeignKey('games.game_id'))
    given_by = Column(Integer, ForeignKey('users.user_id'))
    clue_text = Column(Text, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False)

    game = relationship('Game', back_populates='clue')
    user = relationship('User', back_populates='clue')


class Move(Base):
    __tablename__ = 'moves'

    move_id = Column(Integer, primary_key=True)
    game_id = Column(Integer, ForeignKey('games.game_id'))
    card_id = Column(Integer, ForeignKey('cards.card_id'))
    chosen_by = Column(Integer, ForeignKey('users.user_id'))
    created_at = Column(TIMESTAMP, nullable=False)

    game = relationship('Game', back_populates='move')
    card = relationship('Card', back_populates='move')
    user = relationship('User', back_populates='move')
