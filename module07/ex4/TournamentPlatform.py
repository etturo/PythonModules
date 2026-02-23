#!/usd/bin/env python3
from ex4.TournamentCard import TournamentCard


class TournamentPlatform():
    _card_registered: list[TournamentCard] = []
    _number_of_matches: int = 0
    _status: str = "Inactive"

    def register_card(self,
                      card: TournamentCard) -> str:
        self._card_registered.append(card)

    def create_match(self,
                     card1_id: str,
                     card2_id: str) -> dict:
        self._status = "Active"

        card1: TournamentCard = next(
            card for card in self._card_registered
            if card._info['name'] == card1_id)

        card2: TournamentCard = next(
            card for card in self._card_registered
            if card._info['name'] == card2_id)

        if card1._info['cost'] >= card2._info['cost']:
            winner: TournamentCard = card1
            loser: TournamentCard = card2
        else:
            winner: TournamentCard = card2
            loser: TournamentCard = card1

        winner.update_wins(1)
        winner._rating += 8
        loser.update_losses(1)
        loser._rating -= 8

        self._number_of_matches += 1

        return {"winner": winner,
                "loser": loser,
                "winner_rating": winner._rating,
                "loser_rating": loser._rating}

    def get_leaderboard(self) -> list:
        return sorted(self._card_registered,
                      key=lambda card: card._rating,
                      reverse=True)

    def generate_tournament_report(self) -> dict:
        total_rating: int = 0
        avarage_rating: float

        for card in self._card_registered:
            total_rating += card._rating

        avarage_rating = total_rating / len(self._card_registered)

        return {'total_card': len(self._card_registered),
                'matches_played': self._number_of_matches,
                'avg_rating': avarage_rating,
                'platform_status': self._status}
