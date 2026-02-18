#!/usr/bin/env python3
from .Deck import Deck, CreatureCard, ArtifactCard, SpellCard
from card_generator import CardGenerator

if __name__ == "__main__":
    print("\n=== DataDeck Deck Builder ===\n")

    deck = Deck()
    gen = CardGenerator()

    deck.add_card(CreatureCard(*gen.get_random_creature()))
    deck.add_card(ArtifactCard(*gen.get_random_artifact()))
    deck.add_card(SpellCard(*gen.get_random_spell()))
    print("Building deck with different card types...")
    print(f"Deck stats: {deck.get_deck_stats()}")
