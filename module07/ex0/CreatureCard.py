#!/usr/bin/env python3
from Card import Card
from enum import Enum


class CreatureName(Enum):
    "Fire Dragon" : 1


class CreatureCard(Card):
    def __init__(self,
                 name: str,
                 cost: int,
                 rarity: str,
                 attack: int,
                 health: int) -> None:
        self.name: str = name
        self.cost: int = cost
        self.rarity: str = rarity
        self.attack: int = attack
        self.health: int = health
        return

    def play(self,
             game_state: dict) -> dict:
        pass

    def attack_target(self,
                      target) -> dict:
        pass
