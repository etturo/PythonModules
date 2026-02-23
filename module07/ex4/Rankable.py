#!/usd/bin/env python3
from abc import ABC, abstractmethod


class Rankable(ABC):
    _wins: int = 0
    _loss: int = 0

    @abstractmethod
    def calculate_rating(self) -> int:
        pass

    def update_wins(self,
                    wins: int) -> None:
        self._wins += wins

    def update_losses(self,
                      losses: int) -> None:
        self._loss += losses

    def get_rank_info(self) -> dict:
        return {
            'wins': self._wins,
            'losses': self._loss,
            'rating': self.calculate_rating()
        }
