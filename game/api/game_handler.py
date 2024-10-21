from enum import Enum


class GameStatus(Enum):
    INIT = 1
    CREATED = 2
    STARTED = 3
    FINISHED = 4


class GamePlayerRole(Enum):
    CAPTAIN = 1
    PLAYER = 2


class GameColor(Enum):
    """It's a color for teams, cards and players"""

    WHITE = 0
    BLACK = 1
    RED = 2
    BLUE = 3


class CardStatus(Enum):
    NOT_CLICKED = 0
    CLICKED = 1
