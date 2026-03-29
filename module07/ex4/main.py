from .TournamentCard import TournamentCard
from .TournamentPlatform import TournamentPlatform


def main() -> None:
    print("=== DataDeck Tournament Platform ===")
    print("\nRegistering Tournament Cards...")

    platform = TournamentPlatform()

    fire_dragon = TournamentCard(
        name="Fire Dragon",
        cost=5,
        rarity="Legendary",
        attack_power=7,
        health=12,
        card_id="dragon_001",
        rating=1200,
    )
    ice_wizard = TournamentCard(
        name="Ice Wizard",
        cost=4,
        rarity="Epic",
        attack_power=5,
        health=10,
        card_id="wizard_001",
        rating=1150,
    )

    platform.register_card(fire_dragon)
    platform.register_card(ice_wizard)

    for card in [fire_dragon, ice_wizard]:
        stats = card.get_tournament_stats()
        print(f"\n{card.name} (ID: {card.card_id}):")
        print("- Interfaces: [Card, Combatable, Rankable]")
        print(f"- Rating: {stats['rating']}")
        print(f"- Record: {stats['record']}")

    print("\nCreating tournament match...")
    match_result = platform.create_match("dragon_001", "wizard_001")
    print(f"Match result: {match_result}")

    print("\nTournament Leaderboard:")
    leaderboard = platform.get_leaderboard()
    for index, entry in enumerate(leaderboard, start=1):
        print(f"{index}. {entry['name']} - "
              f"Rating: {entry['rating']} ({entry['record']})")

    print("\nPlatform Report:")
    report = platform.generate_tournament_report()
    print(report)
    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!?")


if __name__ == "__main__":
    main()
