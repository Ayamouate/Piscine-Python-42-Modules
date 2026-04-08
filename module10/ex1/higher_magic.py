from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    return lambda *args, **kwargs: (
        spell1(*args, **kwargs),
        spell2(*args, **kwargs)
    )


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    return lambda *args, **kwargs: base_spell(
        *(arg * multiplier for arg in args),
        **kwargs
    )


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    return lambda *args, **kwargs: (
        spell(*args, **kwargs)
        if condition(*args, **kwargs)
        else "Spell fizzled"
    )


def spell_sequence(spells: list[Callable]) -> Callable:
    return lambda *args, **kwargs: [
        spell(*args, **kwargs) for spell in spells
    ]


def main() -> None:
    # Test functions
    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target} for {power} damage"

    def heal(target: str, power: int) -> str:
        return f"Heals {target} for {power} HP"

    print("\nTesting spell combiner...")
    combined = spell_combiner(fireball, heal)
    result1, result2 = combined("Dragon", 10)
    print(f"Combined spell result: {result1.split(' for')[0]}"
          f", {result2.split(' for')[0]}")

    print("\nTesting power amplifier...")
    mega_fireball = power_amplifier(fireball, 3)
    original_power = 10
    mega_fireball("Dragon", original_power)
    amplified_power = original_power * 3
    print(f"Original: {original_power}, Amplified: {amplified_power}")


if __name__ == "__main__":
    main()
