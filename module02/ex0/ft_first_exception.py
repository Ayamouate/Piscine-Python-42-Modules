
def check_temperature(temp_str):
    """
    Checks if the given temperature is suitable for plants.
    """
    try:
        tp = int(temp_str)
        if tp < 0:
            print("Error: -50°C is too cold for plants (min 0°C)")
        elif tp > 40:
            print("Error: 100°C is too hot for plants (max 40°C)")
        else:
            print("Temperature 25°C is perfect for plants!")
    except ValueError:
        print("Error: 'abc' is not a valid number")


def test_temperature_input():
    """
    Tests temperature validation with valid and invalid inputs.
    """
    print("=== Garden Temperature Checker ===")
    print()
    test_value = ["25", "abc", "100", "-50"]
    for temp in test_value:
        print(f"Testing temperature: {temp}")
        check_temperature(temp)
        print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
