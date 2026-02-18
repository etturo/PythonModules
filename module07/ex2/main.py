#!/usr/bin/env python3
from .EliteCard import EliteCard


if __name__ == "__main__":
    print("\n=== DataDeck Ability System ===\n")

    elite_card = EliteCard('Arcane Warrior', )
    print("EliteCard capabilities:")
    print(f"- Card: {elite_card.card_capabilities}")
    print(f"- Combatable: {elite_card.combatable_capabilities}")
    print(f"- Magical: {elite_card.magical_capabilities}")

    print()

    print("Playing Arcane Warrior (Elite Card):")

    print()

    print("Combat phase:")
    elite_card.attack('enemy')
