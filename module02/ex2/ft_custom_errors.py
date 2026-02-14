class GardenError(Exception):
    """Base exception for garden-related errors."""
    pass


class PlantError(GardenError):
    """Raised when a plant health issue is detected."""
    pass


class WaterError(GardenError):
    """Raised when watering conditions are insufficient."""
    pass


def check_plant(days: int, name: str):
    """Checks plant condition and raises PlantError if unhealthy."""
    if days >= 3:
        raise PlantError(f"The {name} plant is wilting!")


def check_watering(water: int):
    """Checks water level and raises WaterError if too low."""
    if water < 70:
        raise WaterError(" Not enough water in the tank!")


def test_custom_errors(days: int, name: str, water: int):
    """
    Demonstrates custom exception handling in a garden system.
    """
    print("=== Custom Garden Errors Demo ===")
    print("\nTesting PlantError...")
    try:
        check_plant(days, name)
    except PlantError as message:
        print("Caught PlantError:", message)
    print("\nTesting WaterError...")
    try:
        check_watering(water)
    except WaterError as message:
        print("Caught WaterError:", message)
    print("\nTesting catching all garden errors...")
    try:
        check_plant(days, name)
    except GardenError as message:
        print("Caught a garden error:", message)
    try:
        check_watering(water)
    except GardenError as message:
        print("Caught a garden error:", message)
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors(7, "tomato", 50)
