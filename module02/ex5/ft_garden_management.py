class GardenError(Exception):
    """Base exception for garden-related errors."""
    pass


class PlantError(GardenError):
    """Raised when a plant health issue is detected."""
    pass


class WaterError(GardenError):
    """Raised when watering conditions are insufficient."""
    pass


class GardenManager:

    def __init__(self):
        self.plant_list: list[str] = []

    def add_plant(self, plant_name: str):
        """
        add plant to the garden.
        """
        try:
            if not plant_name:
                raise PlantError("Plant name cannot be empty!")
            self.plant_list.append(plant_name)
            print(f"Added {plant_name} successfully")
        except PlantError as message:
            print("Error adding plant:", message)

    def water_plants(self, water: int):
        """
        water all plant.
        """
        print("Opening watering system")
        try:
            if water < 70:
                raise WaterError("Not enough water in tank")
            for plant in self.plant_list:
                print("Watering", plant, "- success")
        except WaterError as message:
            print("Error adding plant:", message)
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, plant_name: str, water: int, sun: int):
        """
        Checking plant health.
        """
        try:
            if plant_name not in self.plant_list:
                raise PlantError("Plant not found!")
            if water < 1:
                raise PlantError(f"Water level {water} is too low (min 1)")
            elif water > 10:
                raise PlantError(f"Water level {water} is too high (max 10)")
            if sun < 2:
                raise PlantError(f"Sun {sun} is too low (min 2)")
            elif sun > 12:
                raise PlantError(f"Sun {sun} is too high (max 12)")
            print(f"{plant_name}: healthy (water: {water}, sun: {sun})")
        except PlantError as message:
            print(f"Error checking {plant_name}:", message)


def test_garden_management():
    """
    Test garden manager.
    """
    print("=== Garden Management System ===")

    manager = GardenManager()

    print("\nAdding plants to garden...")
    manager.add_plant("tomato")
    manager.add_plant("lettuce")
    manager.add_plant("")

    print("\nWatering plants...")
    manager.water_plants(70)

    print("\nChecking plant health...")
    manager.check_plant_health("tomato", 5, 8)
    manager.check_plant_health("lettuce", 15, 8)
    print("\nTesting error recovery...")
    try:
        raise WaterError("Not enough water in the tank")
    except GardenError as message:
        print("Caught GardenError:", message)
    finally:
        print("System recovered and continuing...")

    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
