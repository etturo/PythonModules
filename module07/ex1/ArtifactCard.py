#!/usr/bin/env python3
from ex0 import Card


class ArtifactCard(Card):
    def __init__(self,
                 name: str,
                 cost: int,
                 rarity: str,
                 durability: int,
                 effect: str):
        pass

    def play(self,
             game_stat: dict) -> dict:
        pass

    def activate_ability(self) -> dict:
        pass
