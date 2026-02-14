"""
This program modeling plants using inheritance. A base Plant class is extended
by Flower, Tree, and Vegetable classes, each adding specific
attributes and behaviors.
"""


class Plant:
    """Base class for all plants."""
    def __init__(self, name, height, age):
        """Initialize plant name, height (cm), and age (days)."""
        self.name = name
        self.height = height
        self.age = age

    def show_info(self):
        """Print a generic info line; subclasses override with type details."""
        print(f"{self.name}: {self.height}cm, {self.age} days")


class Flower(Plant):
    """Represents a flower plant."""
    def __init__(self, name, height, age, color):
        """Initialize a flower with a color."""
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        """Display blooming message."""
        print(f"{self.name} is blooming beautifully!", end="\n\n")

    def show_info(self):
        """Print formatted info for Flower."""
        print(f"{self.name} (Flower): {self.height}cm, {self.age} days,"
              f" {self.color} color")


class Tree(Plant):
    """Represents a tree plant."""
    def __init__(self, name, height, age, trunk_diameter):
        """Initialize a tree with trunk diameter."""
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        """Display shade information."""
        print(f"{self.name} provides 78 square meters of shade", end="\n\n")

    def show_info(self):
        """Print formatted info for Tree."""
        print(f"{self.name} (Tree): {self.height}cm, {self.age} days,"
              f" {self.trunk_diameter}cm diameter")


class Vegetable(Plant):
    """Represents a vegetable plant."""
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        """Initialize a vegetable with harvest season and nutrition."""
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def show_info(self):
        """Print formatted info for Vegetable."""
        print(f"{self.name} (Vegetable): {self.height}cm, {self.age} days,"
              f" {self.harvest_season} harvest")
        print(f"{self.name} is rich in vitamin {self.nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===", end="\n\n")

    flower1 = Flower("Rose", 25, 30, "red")
    flower1.show_info()
    flower1.bloom()

    flower2 = Flower("Tulip", 29, 33, "pink")
    flower2.show_info()
    flower2.bloom()

    tree1 = Tree("Oak", 500, 1825, 50)
    tree1.show_info()
    tree1.produce_shade()

    tree2 = Tree("Ash", 1200, 2000, 60)
    tree2.show_info()
    tree2.produce_shade()

    veg1 = Vegetable("Tomato", 80, 90, "summer", "C")
    veg1.show_info()
    print("")
    veg2 = Vegetable("Carrot", 25, 60, "summer", "A")
    veg2.show_info()
