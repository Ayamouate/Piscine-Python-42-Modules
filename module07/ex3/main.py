from .AggressiveStrategy import AggressiveStrategy
from .FantasyCardFactory import FantasyCardFactory
from .GameEngine import GameEngine


def main() -> None:
    print("=== DataDeck Game Engine ===")
    print("\nConfiguring Fantasy Card Game...")

    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    engine = GameEngine()
    engine.configure_engine(factory, strategy)

    print(f"Factory: {factory.__class__.__name__}")
    print(f"Strategy: {strategy.get_strategy_name()}")
    print(f"Available types: {factory.get_supported_types()}")

    print("\nSimulating aggressive turn...")
    hand_preview = ", ".join([f"{card.name} ({card.cost})"
                             for card in engine.hand])
    print(f"Hand: [{hand_preview}]")

    print("\nTurn execution:")
    print(f"Strategy: {strategy.get_strategy_name()}")
    actions = engine.simulate_turn()
    print(f"Actions: {actions}")

    print("\nGame Report:")
    report = engine.get_engine_status()
    print(report)

    print("\nAbstract Factory + Strategy Pattern:"
          "Maximum flexibility achieved!")


if __name__ == "__main__":
    main()
