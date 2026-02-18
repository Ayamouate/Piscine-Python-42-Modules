
alice: set[str] = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
bob: set[str] = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
charlie: set[str] = {'level_10', 'treasure_hunter', 'boss_slayer',
                     'speed_demon', 'perfectionist'}


def player_achievement() -> None:
    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")


def achievement_analytics() -> None:
    print("\n=== Achievement Analytics ===")
    unique: set[str] = alice.union(bob, charlie)
    print(f"All unique achievements: {unique}")
    print(f"Total unique achievements: {len(unique)}")


def common() -> None:
    print(f"\nCommon to all players: {alice.intersection(bob, charlie)}")
    dif1: set[str] = alice.difference(bob, charlie)
    dif2: set[str] = bob.difference(alice, charlie)
    dif3: set[str] = charlie.difference(alice, bob)
    print(f"Rare achievements (1 player): {dif1.union(dif2, dif3)}")


def alice_vs_bob() -> None:
    print(f"\nAlice vs Bob common: {alice.intersection(bob)}")
    print(f"Alice unique: {alice.difference(bob)}")
    print(f"Bob unique: {bob.difference(alice)}")


if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")
    player_achievement()
    achievement_analytics()
    common()
    alice_vs_bob()
