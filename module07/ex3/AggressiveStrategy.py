#!/usr/bin/env python3
from ex0.Card import Card


class AggressiveStrategy():
    def execute_turn(self,
                     hand: list,
                     mana: int) -> dict:
        ordered_hand: list[Card] = sorted(hand,
                                          key=lambda x: x.get('cost', 0))
        hand_to_play: list[Card] = []
        initial_mana: int = mana
        damage_dealt: int = 0
        for card in ordered_hand:
            cost: int = card.get('cost')
            if cost <= mana:
                hand_to_play.append(card)
                mana -= cost
                if hasattr(card, 'attack'):
                    damage_dealt += card.get('attack')
                else:
                    damage_dealt += card.get('cost')
        return {'card_played': hand_to_play,
                'mana_used': initial_mana - mana,
                'target_attacked': 'Enemy',
                'damage_dealt': damage_dealt}

    def get_strategy_name(self) -> str:
        return self.__class__.__name__

    def prioritize_targets(self,
                           available_targets: list) -> list:
        pass
