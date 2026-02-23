#!/usd/bin/env python3
from ex4.TournamentCard import TournamentCard
from ex4.Rankable import Rankable
from ex4.TournamentPlatform import TournamentPlatform


if __name__ == "__main__":
    print("\n=== DataDeck Tournament Platform ===\n")

    print("Registering Tournament Cards...")

    print()

    manager = TournamentPlatform()
    manager.register_card(TournamentCard('Fire Dragon', 4, "Common"))
    print("Fire Dragon (ID: dragon_001):")
    print(TournamentPlatform._card_registered[0].get_tournament_stats())

    print()

    manager.register_card(TournamentCard('Ice Wizard', 2, "Common"))
    print("Ice Wizard (ID: ice_wizard_001)")
    print(TournamentPlatform._card_registered[1].get_tournament_stats())

    print()

    print("Creating tournament match")
