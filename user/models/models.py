from sqlalchemy import Column
from sqlalchemy import Text, Integer, TIMESTAMP, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

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