from .CardFactory import CardFactory
from .GameStrategy import GameStrategy


class GameEngine:
    def __init__(self) -> None:
        self.factory: CardFactory | None = None
        self.strategy: GameStrategy | None = None
        self.hand = []
        self.battlefield = []
        self.turns_simulated = 0
        self.total_damage = 0
        self.cards_created = 0

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy
        self.hand = [
            factory.create_creature("dragon"),
            factory.create_creature("goblin"),
            factory.create_spell("fireball")
        ]
        self.cards_created = len(self.hand)

    def simulate_turn(self) -> dict:
        if self.strategy is None:
            raise RuntimeError("Game engine is not configured with a strategy")
        actions = self.strategy.execute_turn(self.hand, self.battlefield)
        self.turns_simulated += 1
        self.total_damage += actions.get("damage_dealt", 0)
        return actions

    def get_engine_status(self) -> dict:
        if self.strategy is not None:
            strategy_name = self.strategy.get_strategy_name()
        else:
            strategy_name = "Unknown"
        return {
            "turns_simulated": self.turns_simulated,
            "strategy_used": strategy_name,
            "total_damage": self.total_damage,
            "cards_created": self.cards_created,
        }
