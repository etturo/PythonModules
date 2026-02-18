#!/usr/bin/env python3
from ex0 import Card


class CreatureCard(Card):
    def __init__(self,
                 name: str,
                 cost: int,
                 rarity: str,
                 attack: int,
                 health: int) -> None:
        super().__init__(name, cost, rarity)
        self._info = {
            'name': name,
            'cost': cost,
            'rarity': rarity,
            'attack': attack,
            'health': health,
            'type': "Creature"
        }
        return

    def play(self,
             game_state: dict) -> dict:
        if super().is_playable(game_state['mana']) is True:
            return {'card_played': self.get_card_info()['name'],
                    'mana_used': self.get_card_info()['cost'],
                    'effect': 'Creature summoned to battlefield'}
        else:
            return {'card_played': 'None',
                    'mana_used': 0,
                    'effect': 'Nothing happened'}

    def attack_target(self,
                      target: Card) -> dict:
        return {'attacker': self.get_card_info()['name'],
                'target': target.get_card_info()['name'],
                'damage_dealt': self.get_card_info()['attack'],
                'combat_resolved': True}
