#!/usr/bin/env python3
from ex0 import Card, CreatureCard
from .ArtifactCard import ArtifactCard
from .SpellCard import SpellCard


class Deck():
    deck: list[Card] = []

    def add_card(self,
                 card: Card) -> None:
        self.deck.append(card)
        return

    def remove_card(self,
                    card_name: str) -> bool:
        self.deck.pop()
        pass

    def shuffle(self) -> None:
        pass

    def draw_card(self) -> Card:
        return self.deck.pop()

    def get_deck_stats(self) -> dict:
        card_count: int = 0
        creature_count: int = 0
        spell_count: int = 0
        artifact_count: int = 0
        total_cost: int = 0

        card_count = len(self.deck)
        for card in self.deck:
            if isinstance(card, CreatureCard):
                creature_count += 1
            elif isinstance(card, ArtifactCard):
                artifact_count += 1
            elif isinstance(card, SpellCard):
                spell_count += 1
            total_cost += int(card.get_card_info()['cost'])

        avarage_cost: float = round(total_cost / card_count, 2)

        return {'total_card': card_count,
                'creatures': creature_count,
                'spells': spell_count,
                'artifacts': artifact_count,
                'avarage': avarage_cost}
