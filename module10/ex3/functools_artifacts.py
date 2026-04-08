import functools
import operator
from typing import Any
from collections.abc import Callable


def spell_reducer(spells: list[int], operation: str) -> int:
    opr = {
        'add': operator.add,
        'multiply': operator.mul,
        'max': lambda a, b: max(a, b),
        'min': lambda a, b: min(a, b),
    }
    if not spells:
        return 0
    if operation not in opr:
        raise ValueError("Unknown operation!")
    return functools.reduce(opr[operation], spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {
        "fire": functools.partial(base_enchantment, element="fire"),
        "ice": functools.partial(base_enchantment, element="ice"),
        "lightning": functools.partial(base_enchantment, element="lightning"),
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @functools.singledispatch
    def cast(spell):
        return "Unknown spell type"

    @cast.register(int)
    def _(spell):
        return f"Damage spell: {spell} damage!"

    @cast.register(str)
    def _(spell):
        return f"Enchantment: {spell}"

    @cast.register(list)
    def _(spell):
        return f"Multi-cast: {len(spell)} spells"
    return cast


def main() -> None:
    def base_enchantment(power: int, element: str, target: str) -> str:
        return f"{element} enchantment with {power} power on {target}"
    try:
        print("\nTesting spell reducer...")
        spells = [10, 20, 30, 40]
        print(f"Sum: {spell_reducer(spells, 'add')}")
        print(f"Product: {spell_reducer(spells, 'multiply')}")
        print(f"Max: {spell_reducer(spells, 'max')}")

        print("\nTesting memoized fibonacci...")
        print(f"Fib(0): {memoized_fibonacci(0)}")
        print(f"Fib(1): {memoized_fibonacci(1)}")
        print(f"Fib(10): {memoized_fibonacci(10)}")
        print(f"Fib(15): {memoized_fibonacci(15)}")

        print("\nTesting spell dispatcher...")
        caster = spell_dispatcher()
        print(caster(42))
        print(caster("fireball"))
        print(caster([1, 2, 3]))
        print(caster(3.14))
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
