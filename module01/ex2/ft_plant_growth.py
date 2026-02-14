class Plant:
    """
    Represent a plant with a name, height, and age.

    Parameters
    ----------
    name : str
        The plant's name.
    height : int or float
        The plant's height in centimeters.
    ag : int
        The plant's age in days.
    """
    def __init__(self, name, height, ag):
        self.name = name
        self.height = height
        self.ag = ag

    def grow(self):
        """plant grows 6 cm"""
        self.height += 6

    def age(self):
        """plant grows 6 days"""
        self.ag += 6

    def get_info(self):
        return f"{self.name}: {self.height}cm, {self.ag} days old"


if __name__ == "__main__":
    print("=== Day 1 ===")
    pl1 = Plant("Rose", 25, 30)
    print(pl1.get_info())
    print("=== Day 7 ===")
    pl1.grow()
    pl1.age()
    print(pl1.get_info())
    print("Growth this week: +6cm")
