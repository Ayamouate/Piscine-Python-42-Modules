
def water_plants(plant_list):
    """
    Waters each plant in the given list.
    Raises an error if an invalid plant (None) is found.
    """
    print("Opening watering system")
    try:
        for p in plant_list:
            if p is None:
                raise TypeError("invalid plant!")
            print(f"Watering {p}")
    except TypeError as message:
        print("Error: Cannot water None -", message)
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    """
    Tests normal watering and error handling of the watering system.
    """
    print("=== Garden Watering System ===")
    print("\nTesting normal watering...")
    plants = ["tomato", "lettuce", "carrots"]
    water_plants(plants)
    print("Watering completed successfully!")
    print("\nTesting with error...")
    pl = ["tomato", None, "carrots"]
    water_plants(pl)
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
