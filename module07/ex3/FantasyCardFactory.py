#!/usr/bin/env python3
from .CardFactory import CardFactory
from ex0 import Card
import random


class FantasyCardFactory(CardFactory):
    _creatures = [
        {"name": "Fire Dragon", "cost": 5, "rarity": "Legendary",
            "attack": 7, "health": 5},
        {"name": "Goblin Warrior", "cost": 2, "rarity": "Common",
            "attack": 2, "health": 1},
        {"name": "Ice Wizard", "cost": 4, "rarity": "Rare",
            "attack": 3, "health": 4},
        {"name": "Lightning Elemental", "cost": 3, "rarity": "Uncommon",
            "attack": 4, "health": 2},
        {"name": "Stone Golem", "cost": 6, "rarity": "Rare",
            "attack": 5, "health": 8},
        {"name": "Shadow Assassin", "cost": 3, "rarity": "Uncommon",
            "attack": 5, "health": 2},
        {"name": "Healing Angel", "cost": 4, "rarity": "Rare",
            "attack": 2, "health": 6},
        {"name": "Forest Sprite", "cost": 1, "rarity": "Common",
            "attack": 1, "health": 1},
    ]

    _spells = [
        {"name": "Lightning Bolt", "cost": 3, "rarity": "Common",
            "effect_type": "Deals 3 damage to target"},
        {"name": "Healing Potion", "cost": 2, "rarity": "Common",
            "effect_type": "Restores 3 health to target"},
        {"name": "Fireball", "cost": 4, "rarity": "Uncommon",
            "effect_type": "Deals 6 damage to target"},
        {"name": "Shield Spell", "cost": 1, "rarity": "Common",
            "effect_type": "Gives +2 health to target"},
        {"name": "Meteor", "cost": 8, "rarity": "Legendary",
            "effect_type": "Deals 10 damage to all enemies"},
        {"name": "Ice Shard", "cost": 2, "rarity": "Common",
            "effect_type": "Freezes target for 1 turn"},
        {"name": "Divine Light", "cost": 5, "rarity": "Rare",
            "effect_type": "Fully restores health to target"},
        {"name": "Magic Missile", "cost": 1, "rarity": "Common",
            "effect_type": "Deals 1 damage to random enemy"},
    ]

    _artifacts = [
        {"name": "Mana Crystal", "cost": 2, "rarity": "Common",
            "durability": 5, "effect": "Permanent: +1 mana per turn"},
        {"name": "Sword of Power", "cost": 3, "rarity": "Uncommon",
            "durability": 3,
            "effect": "Permanent: +2 attack to equipped creature"},
        {"name": "Ring of Wisdom", "cost": 4, "rarity": "Rare",
            "durability": 4,
            "effect": "Permanent: Draw an extra card each turn"},
        {"name": "Shield of Defense", "cost": 5, "rarity": "Rare",
            "durability": 6,
            "effect": "Permanent: +3 health to all friendly creatures"},
        {"name": "Crown of Kings", "cost": 7, "rarity": "Legendary",
            "durability": 8,
            "effect": "Permanent: +1 cost reduction to all cards"},
        {"name": "Boots of Speed", "cost": 2, "rarity": "Uncommon",
            "durability": 2,
            "effect": "Permanent: Cards cost 1 less mana"},
        {"name": "Cloak of Shadows", "cost": 3, "rarity": "Uncommon",
            "durability": 3,
            "effect": "Permanent: Creatures have stealth"},
        {"name": "Staff of Elements", "cost": 6, "rarity": "Legendary",
            "durability": 7,
            "effect": "Permanent: +1 spell damage"},
    ]

    def create_creature(self,
                        name_or_power: str | int | None = None) -> Card:
        for card in self._creatures:
            if card['name'] == name_or_power and \
               card['attack'] == name_or_power:
                return card
        return random.choice(self._creatures)

    def create_spell(self,
                     name_or_power: str | int | None = None) -> Card:
        for card in self._spells:
            if card['name'] == name_or_power and \
               card['attack'] == name_or_power:
                return card
        return random.choice(self._spells)

    def create_artifact(self,
                        name_or_power: str | int | None = None) -> Card:
        for card in self._spells:
            if card['name'] == name_or_power and \
               card['attack'] == name_or_power:
                return card
        return random.choice(self._artifacts)

    def create_themed_deck(self,
                           size: int) -> list[Card]:
        new_deck: list[Card] = []

        for i in range(size):
            if i % 3:
                new_deck.append(self.create_creature())
            elif i % 5:
                new_deck.append(self.create_spell())
            elif i % 7:
                new_deck.append(self.create_artifact())

        return new_deck

    def get_supported_types(self) -> list:
        return ['creatures',
                'spells',
                'artifact']
