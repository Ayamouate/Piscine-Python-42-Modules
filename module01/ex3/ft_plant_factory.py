"""Main program that creates multiple plants and displays their details."""


class Plant:
    """Represent a plant with a name, height, and age."""
    def __init__(self, name, start_height, start_age):
        self.name = name
        self.height = start_height
        self.age = start_age


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    pl1 = Plant("Rose", 25, 30)
    pl2 = Plant("Oak", 200, 365)
    pl3 = Plant("Cactus", 5, 90)
    pl4 = Plant("Sunflower", 80, 45)
    pl5 = Plant("Fern", 15, 120)
    print(f"Created: {pl1.name} ({pl1.height}cm, {pl1.age} days)")
    print(f"Created: {pl2.name} ({pl2.height}cm, {pl2.age} days)")
    print(f"Created: {pl3.name} ({pl3.height}cm, {pl3.age} days)")
    print(f"Created: {pl4.name} ({pl4.height}cm, {pl4.age} days)")
    print(f"Created: {pl5.name} ({pl5.height}cm, {pl5.age} days)", end="\n\n")
    print("Total plants created: 5")
