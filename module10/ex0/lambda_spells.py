from typing import List


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    sorted_artifact = sorted(artifacts, key=lambda x: x['power'], reverse=True)
    return sorted_artifact


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    filtered_mages = list(filter(lambda x: x['power'] >= min_power, mages))
    return filtered_mages


def spell_transformer(spells: list[str]) -> list[str]:
    transformed_spell = list(map(lambda x: "* " + x + " *", spells))
    return transformed_spell


def mage_stats(mages: list[dict]) -> dict:
    powers = list(map(lambda x: x['power'], mages))
    return {
        "max_power": max(powers),
        "min_power": min(powers),
        "avg_power": round(sum(powers) / len(powers), 2)
    }


def main() -> None:
    print("\nTesting artifact sorter...")
    artifacts = [
        {'name': 'Crystal Orb', 'power': 85, 'type': 'armor'},
        {'name': 'Fire Staff', 'power': 92, 'type': 'focus'}
    ]
    artf: List[dict] = artifact_sorter(artifacts)
    print(f"{artf[0]['name']} ({artf[0]['power']} power)",
          f"comes before {artf[1]['name']} ({artf[1]['power']} power)")

    print("\nTesting spell transformer...")
    spells = spell_transformer(['fireball', 'heal', 'shield'])
    print(" ".join(spells))


if __name__ == "__main__":
    main()
