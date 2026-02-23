#!/usr/bin/env python3
from ex1.Deck import Deck, CreatureCard, ArtifactCard, SpellCard
from card_generator import CardGenerator

if __name__ == "__main__":
    hand: list = []

    print("\n=== DataDeck Deck Builder ===\n")

    deck = Deck()
    gen = CardGenerator()
    game_state = {"mana": 90}

    deck.add_card(CreatureCard(*gen.get_random_creature().values()))
    deck.add_card(ArtifactCard(*gen.get_random_artifact().values()))
    deck.add_card(SpellCard(*gen.get_random_spell().values()))

    print("Building deck with different card types...")
    print(f"Deck stats: {deck.get_deck_stats()}")

    print()

    print("Drawing and playing cards:")
    hand.append(deck.draw_card())
    print(f"Drew: {hand[0].get_card_info()['name']} "
          f"({hand[0].get_card_info()['type']})")
    print("Play result: "
          f"{hand[0].play(game_state)}")
    hand.pop()

    print()
    hand.append(deck.draw_card())
    print(f"Drew: {hand[0].get_card_info()['name']} "
          f"({hand[0].get_card_info()['type']})")
    print("Play result: "
          f"{hand[0].play(game_state)}")
    hand.pop()

    print()
    hand.append(deck.draw_card())
    print(f"Drew: {hand[0].get_card_info()['name']} "
          f"({hand[0].get_card_info()['type']})")
    print("Play result: "
          f"{hand[0].play(game_state)}")
    hand.pop()

    print()

    print("Polymorphism in action: Same interface, different card behaviors!")
