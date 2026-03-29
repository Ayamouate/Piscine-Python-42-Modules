from .Combatable import Combatable
from .Magical import Magical
from ex0.Card import Card


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str) -> None:
        super().__init__(name, 6, "Epic")
        self.mana = 4
        self.health = 10

    def attack(self, target) -> dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage": 5,
            "combat_type": "melee"
        }

    def defend(self, incoming_damage: int) -> dict:
        blocked = 3
        taken = incoming_damage - blocked
        self.health -= taken
        return {
            "defender": self.name,
            "damage_taken": taken,
            "damage_blocked": blocked,
            "still_alive": self.health > 0
        }

    def get_combat_stats(self) -> dict:
        return {
            "attack": 5,
            "health": self.health,
            "defense_block": 3,
        }

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        mana_used = 4
        if self.mana < mana_used:
            return {
                "caster": self.name,
                "spell": spell_name,
                "targets": targets,
                "mana_used": 0,
                "success": False,
                "reason": "Not enough mana"
            }
        self.mana -= mana_used
        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": mana_used
        }

    def channel_mana(self, amount: int) -> dict:
        self.mana += amount
        return {
            "channeled": amount,
            "total_mana": self.mana
        }

    def get_magic_stats(self) -> dict:
        return {
            "mana": self.mana,
            "known_spells": ["Fireball"]
        }

    def play(self, game_state: dict) -> dict:
        print(f"\nPlaying {self.name} (Elite Card):")
        if game_state.get("phase") == "combat":
            return self.attack("Enemy")
        if game_state.get("phase") == "magic":
            return self.cast_spell("Fireball", ["Enemy1"])
        return {
            "card_played": self.name,
            "effect": "No phase action",
        }
