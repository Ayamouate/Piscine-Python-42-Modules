"""
Garden Security System Program.

This program demonstrates a SecurePlant class that protects
the plant's height and age from invalid values. It allows
updating and retrieving these attributes safely while printing
status messages for each operation.
"""


class SecurePlant:
    """class that protects its data from corruption"""
    def __init__(self, name, height, age):
        """SecurePlant class represents a plant with protected attributes."""
        self.name = name
        self.__height = 0
        self.__age = 0
        print(f"Plant created: {self.name}")
        self.set_height(height)
        self.set_age(age)

    def set_height(self, new_height):
        """ Updates the plant's height if the value is valid."""
        if new_height < 0:
            print("Invalid operation attempted:",
                  f"height {new_height}cm [REJECTED]")
            print("Security: Negative height rejected", end="\n\n")
        else:
            self.__height = new_height
            print(f"Height updated: {self.__height}cm [OK]")

    def set_age(self, new_age):
        """ Updates the plant's age if the value is valid."""
        if new_age < 0:
            print("Invalid operation attempted:",
                  f"age {new_age} days [REJECTED]")
            print("Security: Negative age rejected", end="\n\n")
        else:
            self.__age = new_age
            print(f"Age updated: {self.__age} days [OK]", end="\n\n")

    def get_height(self):
        """Returns the current height of the plant."""
        return self.__height

    def get_age(self):
        """Returns the current age of the plant."""
        return self.__age


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant = SecurePlant("Rose", 20, 10)
    plant.set_height(25)
    plant.set_age(30)
    plant.set_height(-5)
    print(f"Current plant: {plant.name}",
          f"({plant.get_height()}cm, {plant.get_age()} days)")
