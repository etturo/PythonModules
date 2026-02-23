#!/usr/bin/env python3
from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy
from ex3.AggressiveStrategy import AggressiveStrategy
from ex0 import Card
from ex3.FantasyCardFactory import FantasyCardFactory


class GameEngine:
    def __init__(self):
        self.turn_simulated: int = 0

    def configure_engine(self,
                         factory: CardFactory,
                         strategy: GameStrategy) -> None:
        print("Configuring Fantasy Card Game...")
        print(f"Factory: {factory.__class__.__name__}")
        print(f"Strategy: {strategy.__class__.__name__}")
        print(f"Available types: {factory.get_supported_types()}")

    def simulate_turn(self) -> dict:
        self.turn_simulated += 1
        factory = FantasyCardFactory()
        strategy = AggressiveStrategy()

        self.configure_engine(factory, strategy)

        print()

        print("Simulating aggressive turn...")
        self.hand: list[Card] = []
        self.hand.append(factory.create_creature())
        self.hand.append(factory.create_spell())
        self.hand.append(factory.create_artifact())
        print(f"Hand: {[card['name'] for card in self.hand]}")

        print()

        print("Turn execution:")
        print(f"Strategy: {strategy.__class__.__name__}")
        print(f"Actions: {strategy.execute_turn(self.hand, 20)}")

        print()

    def get_engine_status(self) -> dict:
        print("Game Report:")
        return {'turn_simulated': self.turn_simulated,
                'strategy_used': 'AggressiveStrategy',
                'cards_created': len(self.hand)}
