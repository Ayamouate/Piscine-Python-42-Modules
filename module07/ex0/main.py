from .CreatureCard import CreatureCard


def main() -> None:
    print("=== DataDeck Card Foundation ===")
    print("\nTesting Abstract Base Class Design:")

    fire_dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)

    print("\nCreatureCard Info:")
    print(fire_dragon.get_card_info())

    mana_available = 6
    print(f"\nPlaying Fire Dragon with {mana_available} mana available:")
    is_playable = fire_dragon.is_playable(mana_available)
    print(f"Playable: {is_playable}")
    if is_playable:
        print(f"Play result: {fire_dragon.play({'mana': mana_available})}")

    print("\nFire Dragon attacks Goblin Warrior:")
    print(f"Attack result: {fire_dragon.attack_target('Goblin Warrior')}")

    low_mana = 3
    print(f"\nTesting insufficient mana ({low_mana} available):")
    print(f"Playable: {fire_dragon.is_playable(low_mana)}")

    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
