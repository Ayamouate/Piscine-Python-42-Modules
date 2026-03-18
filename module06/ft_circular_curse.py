from alchemy.grimoire.validator import validate_ingredients
from alchemy.grimoire.spellbook import record_spell


def main() -> None:
    print("=== Circular Curse Breaking ===")

    print("\nTesting ingredient validation:")
    print("validate_ingredients(\"fire air\"):",
          validate_ingredients("fire air"))
    print("record_spell(\"dragon scales\"):",
          validate_ingredients("dragon scales"))

    print("\nTesting spell recording with validation:")
    print("record_spell(\"Fireball\", \"fire air\"):",
          record_spell("Fireball", "fire air"))
    print("record_spell(\"Dark Magic\", \"shadow\"):",
          record_spell("Dark Magic", "shadow"))

    print("\nTesting late import technique:")
    print("record_spell(\"Lightning\", \"air\"):",
          record_spell("Lightning", "air"))

    print("\nCircular dependency curse avoided using late imports!")
    print("All spells processed safely!")


if __name__ == "__main__":
    main()
