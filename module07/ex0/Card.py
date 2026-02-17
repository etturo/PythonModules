#!/usr/bin/env python3
from abc import ABC


class Card(ABC):
    def __init__(self,
                 name: str,
                 cost: int,
                 rarity: str) -> None:
        pass

    def play(self,
             game_state: dict) -> dict:
        pass

    def get_card_info(self) -> dict:
        pass

    def is_playable(self,
                    available_mana: int) -> bool:
        pass
