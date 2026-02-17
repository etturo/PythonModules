#!/usr/bin/env python3
import alchemy

if __name__ == "__main__":
    print("\n=== Sacred Scroll Mastery ===\n")

    print("Testing direct module access:")
    print("alchemy.elements.create_fire(): "
          f"{alchemy.elements.create_fire()}")
    print("alchemy.elements.create_water(): "
          f"{alchemy.elements.create_water()}")
    print("alchemy.elements.create_earth(): "
          f"{alchemy.elements.create_earth()}")
    print("alchemy.elements.create_air(): "
          f"{alchemy.elements.create_air()}")

    print()

    print("Testing package-level access (controlled by __init__.py):")
    print("alchemy.create_fire(): "
          f"{alchemy.create_fire()}")
    print("alchemy.create_water(): "
          f"{alchemy.create_water()}")
    try:
        print("alchemy.create_earth(): ", end="")
        print(alchemy.create_earth())
    except AttributeError:
        print("AttributeError - not exposed")
    try:
        print("alchemy.create_air(): ", end="")
        print(alchemy.create_air())
    except AttributeError:
        print("AttributeError - not exposed")

    print()

    print("Package metadata:")
    print(f"Version: {alchemy.__version__}")
    print(f"Author: {alchemy.__author__}")
