#!/usd/bin/env python3
from ex4.Rankable import Rankable
from ex0.Card import Card
from ex2.Combatable import Combatable


class TournamentCard(Rankable, Card, Combatable):
    _rating: int = 1000

    def play(self,
             game_state: dict) -> dict:
        pass

    def attack(self,
               target) -> dict:
        pass

    def calculate_rating(self) -> int:
        return self._rating

    def get_tournament_stats(self) -> dict:
        return ("- Interfaces: "
                f"{[base.__name__ for base in TournamentCard.__bases__]}\n"
                "- Rating: "
                f"{self._rating}\n"
                "- Record "
                f"{self._wins}-{self._loss}")

    def defend(self,
               incoming_damage: int) -> dict:
        pass

    def get_combat_stat(self):
        pass
