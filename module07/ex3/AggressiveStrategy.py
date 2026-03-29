from .GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        mana_budget = 5
        played_cards: list[str] = []
        mana_used = 0
        damage_dealt = 0

        playable = sorted(hand, key=lambda card: card.cost)
        for card in playable:
            if mana_used + card.cost > mana_budget:
                continue
            played_cards.append(card.name)
            mana_used += card.cost

            if card.__class__.__name__ == "CreatureCard":
                damage_dealt += getattr(card, "attack", 0)
            elif card.__class__.__name__ == "SpellCard":
                if "3 damage" in getattr(card, "effect", ""):
                    damage_dealt += 3

        targets = self.prioritize_targets(["Enemy Player"])
        return {
            "cards_played": played_cards,
            "mana_used": mana_used,
            "targets_attacked": targets,
            "damage_dealt": damage_dealt,
        }

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        if "Enemy Player" in available_targets:
            return ["Enemy Player"]
        return available_targets
