#!/usr/bin/env python3
from ex0 import Card
from .FantasyCardFactory import FantasyCardFactory
from .GameEngine import GameEngine
from .AggressiveStrategy import AggressiveStrategy


if __name__ == "__main__":
    print("\n=== DataDeck Game Engine ===\n")

    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()

    print("Configuring Fantasy Card Game...")
    print(f"Factory: {factory.__class__.__name__}")
    print(f"Strategy: {strategy.__class__.__name__}")
    print(f"Available types: {factory.get_supported_types()}")

    print()

    print("Simulating aggressive turn...")
    hand: list[Card] = []
    hand.append(factory.create_creature())
    hand.append(factory.create_spell())
    hand.append(factory.create_artifact())
    print(f"Hand: {[card['name'] for card in hand]}")
