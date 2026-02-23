#!/usd/bin/env python3
from ex4.TournamentCard import TournamentCard


class TournamentPlatform():
    _card_registered: list[TournamentCard] = []

    def register_card(self,
                      card: TournamentCard) -> str:
        self._card_registered.append(card)

    def create_match(self,
                     card1_id: str,
                     card2_id: str) -> dict:
        pass

    def get_leaderboard(self) -> list:
        pass

    def generate_tournament_report(self) -> dict:
        pass
