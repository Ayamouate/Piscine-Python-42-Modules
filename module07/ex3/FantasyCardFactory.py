from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from .CardFactory import CardFactory


class FantasyCardFactory(CardFactory):
    def __init__(self) -> None:
        self._supported_types = {
            "creatures": ["dragon", "goblin"],
            "spells": ["fireball"],
            "artifacts": ["mana_ring"],
        }

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        creature = str(name_or_power or "dragon").lower()
        if creature == "goblin":
            return CreatureCard("Goblin Warrior", 2, "Common", 5, 2)
        return CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        spell = str(name_or_power or "fireball").lower()
        if spell == "fireball":
            return SpellCard("Lightning Bolt", 3, "Common",
                             "Deal 3 damage to target")
        return SpellCard("Arcane Blast", 2, "Common",
                         "Deal 2 damage to target")

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        artifact = str(name_or_power or "mana_ring").lower()
        if artifact == "mana_ring":
            return ArtifactCard("Mana Ring", 2, "Rare", 3,
                                "Permanent: +1 mana per turn")
        return ArtifactCard("Runed Totem", 3, "Common", 2,
                            "Permanent: +1 attack to creatures")

    def create_themed_deck(self, size: int) -> dict:
        cards = [
            self.create_creature("dragon"),
            self.create_creature("goblin"),
            self.create_spell("fireball"),
        ]
        if size > len(cards):
            cards.extend(self.create_artifact("mana_ring")
                         for _ in range(size - len(cards)))
        return {"cards": cards[:size], "theme": "fantasy"}

    def get_supported_types(self) -> dict:
        return self._supported_types.copy()
