from ex1.Deck import Deck
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex0.CreatureCard import CreatureCard


def main() -> None:
    print("=== DataDeck Deck Builder ===")

    print("\nBuilding deck with different card types...")
    deck = Deck()

    spell = SpellCard("Lightning Bolt", 3, "Common",
                      "Deal 3 damage to target")
    artifact = ArtifactCard("Mana Crystal", 2, "Uncommon",
                            3, "Permanent: +1 mana per turn")
    creature = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)

    deck.add_card(spell)
    deck.add_card(artifact)
    deck.add_card(creature)

    stats = deck.get_deck_stats()
    print(f"Deck stats: {stats}")

    print("\nDrawing and playing cards:")
    game_state = {"mana": 10}

    for _ in range(3):
        card = deck.draw_card()
        if card:
            card_type = card.__class__.__name__.replace('Card', '')
            print(f"\nDrew: {card.name} ({card_type})")
            result = card.play(game_state)
            print(f"Play result: {result}")

    print("\nPolymorphism in action: Same interface,"
          "different card behaviors!")


if __name__ == "__main__":
    main()
