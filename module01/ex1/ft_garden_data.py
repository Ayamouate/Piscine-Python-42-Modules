"""
program that manages data for at least three different plants and displays
their information in an organized way.
"""


class Plant:
    """
    Represent a plant with a name, height, and age.

    Parameters
    ----------
    name : str
        The plant's name.
    height : int or float
        The plant's height in centimeters.
    age : int
        The plant's age in days.
    """
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    pl1 = Plant("Rose", 25, 30)
    pl2 = Plant("Sunflower", 80, 45)
    pl3 = Plant("Cactus", 15, 120)
    print(f"{pl1.name}: {pl1.height}cm, {pl1.age} days old")
    print(f"{pl2.name}: {pl2.height}cm, {pl2.age} days old")
    print(f"{pl3.name}: {pl3.height}cm, {pl3.age} days old")
