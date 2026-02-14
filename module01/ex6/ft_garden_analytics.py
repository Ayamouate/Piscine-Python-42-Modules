"""
Garden data analytics platform demonstrating advanced OOP concepts.

- GardenManager handles multiple gardens
- Nested GardenStats helper calculates analytics
- Inheritance chain: Plant → FloweringPlant → PrizeFlower
- Class methods, instance methods, static methods, and non-member functions
"""


class GardenManager:
    """ Manages multiple gardens and provides global operations."""
    class GardenStats:
        """Nested helper responsible ONLY for analytics"""
        def __init__(self, gardens):
            """Initialize statistics with a list of gardens."""
            self.gardens = gardens

        def total_gardens(self):
            return len(self.gardens)

        def garden_score(self):
            """Calculate garden score: sum of heights + prize points × 4."""
            scores = {}
            for garden in self.gardens:
                total_height = sum(p.height for p in garden.plants)
                prize_bonus = sum(p.prize for p in garden.plants)
                scores[garden.owner] = total_height + (prize_bonus * 4)
            return scores

    def __init__(self):
        """Initialize the garden manager."""
        self.gardens = []

    def add_garden(self, garden):
        """Add a garden to the manager."""
        self.gardens.append(garden)

    @staticmethod
    def validate_height(height):
        return height > 0

    @classmethod
    def create_garden_network(cls):
        """Create and return a predefined garden network."""
        manager = cls()
        alice = Garden("Alice")
        bob = Garden("Bob")
        manager.add_garden(alice)
        manager.add_garden(bob)
        return manager


class Garden:
    """Represents a single garden and its data"""
    def __init__(self, owner_name):
        self.owner = owner_name
        self.plants = []
        self.growth = 0

    def add_plant(self, plant):
        self.plants.append(plant)
        print("Added", plant.name, "to", self.owner + "'s garden")

    def help_plants_grow(self):
        print(self.owner, "is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            self.growth += 1

    def report(self):
        print("=== " + self.owner + "'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            plant.describe()
        print("")
        print(f"Plants added: {len(self.plants)}, "
              f"Total growth: {self.growth}cm")

        # Count plant types dynamically
        type_counts = {"regular": 0, "flowering": 0, "prize": 0}
        for p in self.plants:
            if p.prize > 0:
                type_counts["prize"] += 1
            elif hasattr(p, "color"):
                type_counts["flowering"] += 1
            else:
                type_counts["regular"] += 1

        print(f"Plant types: {type_counts['regular']} regular, "
              f"{type_counts['flowering']} flowering, "
              f"{type_counts['prize']} prize flowers")


class Plant:
    """Base plant entity"""
    def __init__(self, name, height):
        self.name = name
        self.height = height
        self.prize = 0

    def grow(self):
        self.height += 1
        print(self.name, "grew 1cm")

    def describe(self):
        print(f"- {self.name}: {self.height} cm")


class FloweringPlant(Plant):
    """Specialized plant with flowering behavior"""
    def __init__(self, name, height, color):
        super().__init__(name, height)
        self.color = color

    def describe(self):
        print(f"- {self.name}: {str(self.height)}cm, "
              f"{self.color} flowers (blooming)")


class PrizeFlower(FloweringPlant):
    """Elite plant with prize-related metrics"""
    def __init__(self, name, height, color, prize_point):
        super().__init__(name, height, color)
        self.prize = prize_point

    def describe(self):
        print(f"- {self.name}: {self.height}cm, {self.color}"
              f" flowers (blooming), Prize points: {self.prize}")


if __name__ == "__main__":
    print("=== Garden Management System Demo ===", end="\n\n")
    manager = GardenManager.create_garden_network()

    alice = manager.gardens[0]

    alice.add_plant(Plant("Oak Tree", 100))
    alice.add_plant(FloweringPlant("Rose", 25, "red"))
    alice.add_plant(PrizeFlower("Sunflower", 50, "yellow", 10))
    print("")
    alice.help_plants_grow()
    print("")
    alice.report()
    print("")
    print("Height validation test:", GardenManager.validate_height(1))

    stats = GardenManager.GardenStats(manager.gardens)
    scores = stats.garden_score()
    print("Garden scores - Alice:", scores["Alice"], ", Bob:", scores["Bob"])
    print("Total gardens managed:", stats.total_gardens())
