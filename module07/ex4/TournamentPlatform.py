from .TournamentCard import TournamentCard


class TournamentPlatform:
    def __init__(self) -> None:
        self.cards: dict[str, TournamentCard] = {}
        self.matches_played = 0

    def register_card(self, card: TournamentCard) -> str:
        self.cards[card.card_id] = card
        return card.card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        if card1_id not in self.cards or card2_id not in self.cards:
            raise ValueError("Both card IDs must be registered")

        card1 = self.cards[card1_id]
        card2 = self.cards[card2_id]

        if card1.attack_power >= card2.attack_power:
            winner = card1
            loser = card2
        else:
            winner = card2
            loser = card1

        winner.update_wins(1)
        loser.update_losses(1)
        winner.rating += 16
        loser.rating -= 16
        self.matches_played += 1

        return {
            "winner": winner.card_id,
            "loser": loser.card_id,
            "winner_rating": winner.rating,
            "loser_rating": loser.rating,
        }

    def get_leaderboard(self) -> list:
        ranked_cards = sorted(self.cards.values(),
                              key=lambda card: card.rating, reverse=True)
        return [
            {
                "name": card.name,
                "rating": card.rating,
                "record": f"{card.wins}-{card.losses}",
            }
            for card in ranked_cards
        ]

    def generate_tournament_report(self) -> dict:
        total_cards = len(self.cards)
        average_rating = 0
        if total_cards > 0:
            average_rating = sum(card.rating for card in
                                 self.cards.values()) // total_cards

        return {
            "total_cards": total_cards,
            "matches_played": self.matches_played,
            "avg_rating": average_rating,
            "platform_status": "active",
        }
