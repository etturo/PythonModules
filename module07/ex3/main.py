#!/usr/bin/env python3
from .GameEngine import GameEngine


if __name__ == "__main__":
    print("\n=== DataDeck Game Engine ===\n")

    engine = GameEngine()
    engine.simulate_turn()
    print(f"{engine.get_engine_status()}")

    print()

    print("Abstract Factory + Strategy Pattern: Maximum flexibility achieved!")
