
def check_plant_name(plant_name):
    """
    Validate the plant's name.
    """
    if not plant_name:
        raise ValueError("Plant name cannot be empty!")
    print(f"Plant '{plant_name}' is healthy!")


def check_plant_water_level(water_level):
    """
    Validate the plant's water level.
    """
    if water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")
    elif water_level < 1:
        raise ValueError(f"Water level {water_level} is too low (min 1)")
    print(f"Water level {water_level} is good")


def check_plant_sunlight(sunlight):
    """
    Validate the plant's sunlight exposure.
    """
    if sunlight < 2:
        raise ValueError(f"Sunlight hours {sunlight} is too low (min 2)")
    elif sunlight > 12:
        raise ValueError(f"Sunlight hours {sunlight} is too high (max 12)")
    print(f"Sunlight hours is {sunlight} perfect")


def check_plant_health(plant_name=None, water_level=None, sunlight_hours=None):
    """
    Check the health of a plant.
    """
    if plant_name is not None:
        try:
            check_plant_name(plant_name)
        except ValueError as message:
            print("Error:", message)
    if water_level is not None:
        try:
            check_plant_water_level(water_level)
        except ValueError as message:
            print("Error:", message)
    if sunlight_hours is not None:
        try:
            check_plant_sunlight(sunlight_hours)
        except ValueError as message:
            print("Error:", message)


def test_plant_checks():
    """
    Test different scenarios of plant health checks.
    """
    print("=== Garden Plant Health Checker ===")
    print("\nTesting good values...")
    check_plant_health(plant_name="tomato")
    print("\nTesting empty plant name...")
    check_plant_health(plant_name="")
    print("\nTesting bad water level...")
    check_plant_health(water_level=15)
    print("\nTesting bad sunlight hours...")
    check_plant_health(sunlight_hours=0)
    print("\nAll error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
