from datetime import datetime
from game.api.game_handler import GameStatus
from game.models import models as game_models

DASHBOARD_LIMIT = 25


class Game:
    game_id: int
    created_by: int
    created_at: datetime
    status: GameStatus

    def __init__(self, game_id: int, created_by: int, created_at: datetime, status: GameStatus):
        self.game_id = game_id
        self.created_by = created_by
        self.created_at = created_at
        self.status = status

    def new_cards(self) -> list[game_models.Card]:
        teams_cards = {
            
        }

