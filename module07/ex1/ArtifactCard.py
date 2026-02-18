#!/usr/bin/env python3
from ex0 import Card


class ArtifactCard(Card):
    def __init__(self,
                 name: str,
                 cost: int,
                 rarity: str,
                 durability: int,
                 effect: str):
        super().__init__(name, cost, rarity)
        self._info = {
            'name': name,
            'cost': cost,
            'rarity': rarity,
            'durability': durability,
            'effect': effect,
            'type': "Artifact"
        }

    def play(self,
             game_state: dict) -> dict:
        if super().is_playable(game_state['mana']) is True:
            return {'card_played': self.get_card_info()['name'],
                    'mana_used': self.get_card_info()['cost'],
                    'effect': self._info['effect']}
        else:
            return {'card_played': 'None',
                    'mana_used': 0,
                    'effect': 'Nothing happened'}

    def activate_ability(self) -> dict:
        pass
