#!/usr/bin/env python3
import alchemy.elements
from alchemy.elements import create_fire
from alchemy.potions import healing_potion as heal
from alchemy.elements import create_fire, create_water

if __name__ == "__main__":
    print("\n=== Import Transmutation Mastery ===\n")

    print("Method 1 - Full module import:")
    print("alchemy.elements.create_fire(): "
          f"{alchemy.elements.create_fire()}")

    print()

    print("Method 2 - Specific function import:")
    print(f"create_water(): {create_water()}")

    print()

    print("Method 3 - Aliased import:")
    print(f"heal(): {heal()}")

    print()

    print("Method 4 - Multiple imports:")
    print(f"create_water(): "
          f"{create_water()}")
    print(f"create_fire(): {create_fire()}")
    print(f"strenght_potion(): {stren}")
