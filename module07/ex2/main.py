#!/usr/bin/env python3
from .EliteCard import EliteCard


if __name__ == "__main__":
    print("\n=== DataDeck Ability System ===\n")

    elite_card = EliteCard('Arcane Warrior', 6, 'Leggendary', 5, 4)
    card1 = EliteCard('Warrior1', 3, 'Common', 3, 2)
    card2 = EliteCard('Warrior2', 3, 'Common', 3, 2)
    print("EliteCard capabilities:")
    print(f"- Card: {elite_card.card_capabilities}")
    print(f"- Combatable: {elite_card.combatable_capabilities}")
    print(f"- Magical: {elite_card.magical_capabilities}")

    print()

    print("Playing Arcane Warrior (Elite Card):")

    print()

    print("Combat phase:")
    print(f"Attack result: {elite_card.attack(card1)}")
    print(f"Defense result: {elite_card.defend(5)}")

    print()

    print("Magic phase:")
    print(f"Spell cast: {elite_card.cast_spell('Fireball', [card1, card2])}")
    print(f"Mana channel: {elite_card.channel_mana(2)}")

    print()

    print("Multiple interface implementation successful!")
