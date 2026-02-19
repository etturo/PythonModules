#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import Union


class Card(ABC):
    _info: dict[Union[int, float, str]] = {}

    def __init__(self,
                 name: str,
                 cost: int,
                 rarity: str) -> None:
        self._info = {
            'name': name,
            'cost': cost,
            'rarity': rarity
        }
        return

    @abstractmethod
    def play(self,
             game_state: dict) -> dict:
        pass

    def get_card_info(self) -> dict:
        return self._info

    def is_playable(self,
                    available_mana: int) -> bool:
        if self.get_card_info()['cost'] <= available_mana:
            return True
        return False

    def __repr__(self):
        return self._info['name']
