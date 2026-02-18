#!/usr/bin/env python3
from typing import Dict, List, Any, Optional
import random


class CardGenerator:
    def __init__(self) -> None:
        self._creatures = [
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

        self._spells = [
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

        self._artifacts = [
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

    def get_creature(self, name: str) -> Optional[Dict[str, Any]]:
        for creature in self._creatures:
            if creature["name"] == name:
                return creature.copy()
        return None

    def get_spell(self, name: str) -> Optional[Dict[str, Any]]:
        for spell in self._spells:
            if spell["name"] == name:
                return spell.copy()
        return None

    def get_artifact(self, name: str) -> Optional[Dict[str, Any]]:
        for artifact in self._artifacts:
            if artifact["name"] == name:
                return artifact.copy()
        return None

    def get_random_creature(self) -> Dict[str, Any]:
        return random.choice(self._creatures).copy()

    def get_random_spell(self) -> Dict[str, Any]:
        return random.choice(self._spells).copy()

    def get_random_artifact(self) -> Dict[str, Any]:
        return random.choice(self._artifacts).copy()

    def get_all_creatures(self) -> List[Dict[str, Any]]:
        return [creature.copy() for creature in self._creatures]

    def get_all_spells(self) -> List[Dict[str, Any]]:
        return [spell.copy() for spell in self._spells]

    def get_all_artifacts(self) -> List[Dict[str, Any]]:
        return [artifact.copy() for artifact in self._artifacts]

    def get_cards_by_rarity(self,
                            rarity: str) -> Dict[str, List[Dict[str, Any]]]:
        result = {"creatures": [], "spells": [], "artifacts": []}

        for creature in self._creatures:
            if creature["rarity"] == rarity:
                result["creatures"].append(creature.copy())

        for spell in self._spells:
            if spell["rarity"] == rarity:
                result["spells"].append(spell.copy())

        for artifact in self._artifacts:
            if artifact["rarity"] == rarity:
                result["artifacts"].append(artifact.copy())

        return result

    def get_cards_by_cost(self,
                          max_cost: int) -> Dict[str, List[Dict[str, Any]]]:
        result = {"creatures": [], "spells": [], "artifacts": []}

        for creature in self._creatures:
            if creature["cost"] <= max_cost:
                result["creatures"].append(creature.copy())

        for spell in self._spells:
            if spell["cost"] <= max_cost:
                result["spells"].append(spell.copy())

        for artifact in self._artifacts:
            if artifact["cost"] <= max_cost:
                result["artifacts"].append(artifact.copy())

        return result

    def generate_random_deck(self,
                             deck_size: int = 10) -> List[Dict[str, Any]]:
        all_cards = self._creatures + self._spells + self._artifacts
        deck = []

        for _ in range(deck_size):
            card = random.choice(all_cards).copy()
            deck.append(card)

        return deck
