from enum import Enum
from src.player import Position


class OffensiveStrategy(Enum):
    PICK_AND_ROLL = "Pick and Roll"
    MOTION_OFFENSE = "Motion Offense"
    POST_OFFENSE = "Post Offense"
    FAST_BREAK = "Fast Break"

class DefensiveStrategy(Enum):
    MAN_TO_MAN = "Man-to-Man"
    ZONE_DEFENSE = "Zone Defense"
    PRESS_DEFENSE = "Press Defense"
    BOX_AND_ONE = "Box and One"

class Team:
    def __init__(self, players=None, starters=None, offensive_strategy=None, defensive_strategy=None):
        self.players = players if players else []
        self.starters = starters if starters else {}
        self.offensive_strategy = offensive_strategy
        self.defensive_strategy = defensive_strategy

    def add_player(self, player):
        self.players.append(player)

    def remove_player(self, player):
        if player in self.players:
            self.players.remove(player)

    def set_starters(self, position, player):
        if position in [p.value for p in Position]:
            self.starters[position] = player

    def set_offensive_strategy(self, strategy):
        if strategy in [s.value for s in OffensiveStrategy]:
            self.offensive_strategy = strategy

    def set_defensive_strategy(self, strategy):
        if strategy in [s.value for s in DefensiveStrategy]:
            self.defensive_strategy = strategy

    def __str__(self):
        return f"Team: Players - {len(self.players)}, Starters - {len(self.starters)}, Bench - {len(self.players) - len(self.starters)}, Offensive Strategy - {self.offensive_strategy}, Defensive Strategy - {self.defensive_strategy}"
