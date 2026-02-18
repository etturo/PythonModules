#!/usr/bin/env python3
from ex0 import Card


class SpellCard(Card):
    def __init__(self,
                 name: str,
                 cost: int,
                 rarity: str,
                 effect_type: str):
        self.effect_type = effect_type
        self._info = {'name': name,
                      'cost': cost,
                      'rarity': rarity,
                      'effect_type': self.effect_type}
        return

    def play(self,
             game_state: dict) -> dict:
        return super().play(game_state)

    def resolve_effect(slef,
                       target: list) -> dict:
        pass
