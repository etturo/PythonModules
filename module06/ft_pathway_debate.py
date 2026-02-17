#!/usr/bin/env python3
from alchemy.transmutation import lead_to_gold, stone_to_gem
from alchemy import transmutation
import alchemy

if __name__ == "__main__":
    print("\n=== Pathway Debate Mastery ===\n")

    print("Testing Absolute Imports (from basic.py):")
    print(f"lead_to_gold(): {lead_to_gold()}")
    print(f"stone_to_gem(): {stone_to_gem()}")

    print()

    print("Testing Relative Imports (from advanced.py):")
    print(f"philosopher_stone(): {transmutation.philosopher_stone()}")
    print(f"elixir_of_life(): {transmutation.elixir_of_life()}")

    print()

    print("Testing Package Access:")
    print("alchemy.transmutation.lead_to_gold(): "
          f"{alchemy.transmutation.lead_to_gold()}")
    print("alchemy.transmutation.philosophers_stone(): "
          f"{alchemy.transmutation.philosopher_stone()}")

    print()

    print("Both pathways work! Absolute: clear, Relative: concise")
