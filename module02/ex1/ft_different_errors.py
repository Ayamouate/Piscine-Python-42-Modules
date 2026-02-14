
def garden_operations():
    """
    Demonstrates handling of common Python exceptions using try-except blocks.
    """
    print("\nTesting ValueError...")
    try:
        int("abc")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")
    print("\nTesting ZeroDivisionError...")
    try:
        50 / 0
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
    print("\nTesting FileNotFoundError...")
    try:
        open("missing.txt")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")
    print("\nTesting KeyError...")
    try:
        thisdict = {"brand": "Ford"}
        print(thisdict["missing\\_plant"])
    except KeyError:
        print("Caught KeyError: 'missing\\_plant'")


def test_error_types():
    """
    Tests multiple exception types and shows that program execution continues.
    """
    print("=== Garden Error Types Demo ===")
    garden_operations()
    print("\nTesting multiple errors together...")
    try:
        int("xyz")
        100 / 0
        open("missing.txt")
        thisdict = {"brand": "Ford"}
        print(thisdict["missing\\_plant"])
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
