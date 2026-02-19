#!/usr/bin/env python3
from ex0 import Card
from .Magical import Magical
from .Combatable import Combatable


class EliteCard(Card, Magical, Combatable):
    card_capabilities: list = ['play',
                               'get_card_info',
                               'is_playable']
    combatable_capabilities: list = ['attack',
                                     'defend',
                                     'get_combat_stats']
    magical_capabilities: list = ['cast_spell',
                                  'channel_mana',
                                  'get_magic_stats']

    def __init__(self,
                 name: str,
                 cost: int,
                 rarity: str,
                 attack: int,
                 defense: int):
        super().__init__(name, cost, rarity)
        self._info['attack'] = attack
        self._info['defense'] = defense

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

    def attack(self,
               target) -> dict:
        return {'attacker': self._info['name'],
                'target': target.get_card_info()['name'],
                'damage': self._info['attack'],
                'combat_type': 'melee'}

    def defend(self,
               incoming_damage: int) -> dict:
        if incoming_damage < self._info['defense']:
            damage_blocked: int = incoming_damage
            damage_taken: int = 0
        else:
            damage_blocked: int = self._info['defense']
            damage_taken: int = incoming_damage - self._info['defense']

        if damage_taken > self._info['attack']:
            is_alive: bool = False
        else:
            is_alive: bool = True

        return {'defender': self._info['name'],
                'damage_taken': damage_taken,
                'damage_blocked': damage_blocked,
                'still_alive': is_alive}

    def get_combat_stat(self):
        pass

    def cast_spell(self,
                   spell_name: str,
                   targets: list) -> dict:
        return {'caster': self._info['name'],
                'spell': spell_name,
                'targets': targets,
                'mana_used': self._info['cost']}

    def channel_mana(self,
                     amount: int) -> dict:
        return {'channeled': abs(amount - self._info['cost']),
                'total_mana': amount}

    def get_magic_stats(self) -> dict:
        pass
