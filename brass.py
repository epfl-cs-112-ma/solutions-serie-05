from __future__ import annotations

from collections.abc import Sequence
from typing import Final

class Player:
    name: Final[str] # for identification

    def __init__(self, name: str) -> None:
        self.name = name

    def __repr__(self) -> str:
        return f"Player({repr(self.name)})"

    def __str__(self) -> str:
        return self.name

class IndustryTile:
    owner: Final[Player]
    victory_points: Final[int]
    profitable: bool

    def __init__(self, owner: Player, victory_points: int) -> None:
        self.owner = owner
        self.victory_points = victory_points
        self.profitable = False

    def __repr__(self) -> str:
        return f"IndustryTile({self.owner, self.victory_points, self.profitable})"

class Town:
    name: Final[str] # for identification
    built_industries: Final[list[IndustryTile]]

    def __init__(self, name: str) -> None:
        self.name = name
        self.built_industries = []

    def __repr__(self) -> str:
        return f"Town({self.name})"

    def __str__(self) -> str:
        return self.name

    def build_industry(self, tile: IndustryTile) -> None:
        self.built_industries.append(tile)

class Connection:
    town1: Final[Town]
    town2: Final[Town]
    built_by: Player | None

    def __init__(self, town1: Town, town2: Town) -> None:
        assert town1 is not town2
        self.town1 = town1
        self.town2 = town2
        self.built_by = None

    def __repr__(self) -> str:
        return f"Connection({self.town1}, {self.town2})"

    @property
    def towns(self) -> tuple[Town, Town]:
        return (self.town1, self.town2)

    def build(self, player: Player) -> None:
        assert self.built_by is None
        self.built_by = player

class Game:
    players: Final[list[Player]]
    towns: Final[list[Town]]
    connections: Final[list[Connection]]

    def __init__(
        self,
        players: list[Player],
        towns: list[Town],
        connections: list[Connection]
    ) -> None:
        """Convenient constructor where connections are given as tuples."""
        self.players = players
        self.towns = towns
        self.connections = connections

    def compute_scores(self) -> dict[Player, int]:
        """Computes the scores of all the players in the game."""
        return {p:self.__compute_score(p) for p in self.players}

    def __compute_score(self, player: Player) -> int:
        """Computes the score of the given player."""

        # look, Ma', no loops
        industries_score = sum([
            tile.victory_points
            for town in self.towns
            for tile in town.built_industries
            if tile.owner is player and tile.profitable
        ])
        connections_score = sum([
            1
            for connection in self.connections
            if connection.built_by is player
            for town in connection.towns # using a tuple[Town, Town] as a tuple[Town, ...], because why not?
            for tile in town.built_industries
            if tile.profitable # regardless of who owns it
        ])
        return industries_score + connections_score
