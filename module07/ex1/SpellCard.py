#!/usr/bin/env python3
from ex0.Card import Card


class SpellCard(Card):
    def __init__(self,
                 name: str,
                 cost: int,
                 rarity: str,
                 effect_type: str):
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type
        self._info = {'name': name,
                      'cost': cost,
                      'rarity': rarity,
                      'effect': self.effect_type,
                      'type': "Spell"}
        return

    def play(self,
             game_state: dict) -> dict:
        if super().is_playable(game_state['mana']) is True:
            return {'card_played': self.get_card_info()['name'],
                    'mana_used': self.get_card_info()['cost'],
                    'effect': self.get_card_info()['effect']}
        else:
            return {'card_played': 'None',
                    'mana_used': 0,
                    'effect': 'Nothing happened'}

    def resolve_effect(slef,
                       target: list) -> dict:
        pass
