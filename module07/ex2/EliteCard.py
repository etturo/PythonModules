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

    def attack(self,
               target) -> dict:
        return {'attacker': target}

    def defend(self,
               incoming_damage: int) -> dict:
        pass

    def get_combat_stat(self):
        pass

    def cast_spell(self,
                   spell_name: str,
                   targets: list) -> dict:
        pass

    def channel_mana(self,
                     amount: int) -> dict:
        pass

    def get_magic_stats(self) -> dict:
        pass
