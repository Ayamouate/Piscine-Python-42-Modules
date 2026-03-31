from abc import ABC, abstractmethod
from enum import Enum


class Rarity(Enum):
    COMMON = "Common"
    UNCOMMON = "Uncommon"
    RARE = "Rare"
    EPIC = "Epic"
    LEGENDARY = "Legendary"


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str):
        self.name = name
        self.cost = cost
        self.rarity = rarity if isinstance(rarity, Rarity) else Rarity(rarity)

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        raise NotImplementedError

    def get_card_info(self) -> dict:
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity.value,
        }

    def is_playable(self, available_mana: int) -> bool:
        return available_mana >= self.cost
