from ex0.Card import Card
from ex2.Combatable import Combatable

from .Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, name: str, cost: int, rarity: str,
                 attack_power: int, health: int,
                 card_id: str, rating: int = 1200) -> None:
        super().__init__(name, cost, rarity)
        self.attack_power = attack_power
        self.health = health
        self.card_id = card_id
        self.wins = 0
        self.losses = 0
        self.rating = rating

    def play(self, game_state: dict) -> dict:
        if not self.is_playable(game_state.get("mana", 0)):
            return {"error": "Not enough mana"}
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Tournament card enters the arena",
        }

    def attack(self, target) -> dict:
        target_name = getattr(target, "name", target)
        return {
            "attacker": self.name,
            "target": target_name,
            "damage_dealt": self.attack_power,
            "combat_resolved": True,
        }

    def defend(self, incoming_damage: int) -> dict:
        self.health = max(0, self.health - incoming_damage)
        return {
            "defender": self.name,
            "incoming_damage": incoming_damage,
            "health_remaining": self.health,
            "still_alive": self.health > 0,
        }

    def get_combat_stats(self) -> dict:
        return {
            "attack": self.attack_power,
            "health": self.health,
        }

    def calculate_rating(self) -> int:
        self.rating = max(0, self.rating + (self.wins * 16)
                          - (self.losses * 16))
        return self.rating

    def update_wins(self, wins: int) -> None:
        if wins < 0:
            raise ValueError("wins must be non-negative")
        self.wins += wins

    def update_losses(self, losses: int) -> None:
        if losses < 0:
            raise ValueError("losses must be non-negative")
        self.losses += losses

    def get_rank_info(self) -> dict:
        return {
            "card_id": self.card_id,
            "rating": self.rating,
            "wins": self.wins,
            "losses": self.losses,
        }

    def get_tournament_stats(self) -> dict:
        return {
            "card_id": self.card_id,
            "name": self.name,
            "interfaces": ["Card", "Combatable", "Rankable"],
            "rating": self.rating,
            "record": f"{self.wins}-{self.losses}",
            "attack": self.attack_power,
            "health": self.health,
        }
