from ex0.Card import Card


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect: str):
        super().__init__(name, cost, rarity)
        self.effect = effect
        self.type = "Spell"

    def play(self, game_state: dict) -> dict:
        if game_state.get("mana", 0) < self.cost:
            return {"error": "Not enough mana"}
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": self.effect,
        }

    def resolve_effect(self, targets: list) -> dict:
        e = {}
        for target in targets:
            if self.effect_type == "Damage":
                e[target] = f"{self.name} deals {self.cost} damage to {target}"
            elif self.effect_type == "Heal":
                e[target] = f"{self.name} heals {target} for {self.cost} HP"
        return e
