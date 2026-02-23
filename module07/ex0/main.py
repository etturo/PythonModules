#!/usr/bin/env python3
from ex0.CreatureCard import CreatureCard


if __name__ == "__main__":
    print("\n=== DataDeck Card Foundation ===\n")

    fire_dragon = CreatureCard("Fire Dragon",
                               5,
                               "Leggendary",
                               7,
                               5)
    print("Testing Abstract Base Class Design:\n")
    print(f"Creature Info: {fire_dragon.get_card_info()}")

    print()

    game_state = {'mana': 6}
    print("Playing Fire Dragon with 6 mana available:")
    print(f"Playable: {fire_dragon.is_playable(game_state['mana'])}")
    print(f"Play result: {fire_dragon.play(game_state)}")

    print()

    goblin_warrior = CreatureCard('Goblin Warrior',
                                  3,
                                  'Leggendary',
                                  4,
                                  8)
    print("Fire Dragon attacks Goblin Warrior:")
    print(f"Attack result : {fire_dragon.attack_target(goblin_warrior)}")

    print()

    print("Testing insufficent mana (3 available):")
    print(f"Playable: {fire_dragon.is_playable(3)}")

    print()

    print("Abstract pattern successfully demonstrated!")
