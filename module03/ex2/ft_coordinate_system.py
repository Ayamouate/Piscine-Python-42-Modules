import sys
import math


def parse_number(value: str):
    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except ValueError:
            raise ValueError(f"invalid literal for int() with base 10:"
                             f" '{value}'")


def parse_coordinates_string(value: str) -> tuple:
    if ',' in value:
        parts = value.split(',')
    else:
        parts = value.split()
    if len(parts) != 3:
        raise ValueError(f"Expected 3 coordinates, got {len(parts)}!")
    x = parse_number(parts[0])
    y = parse_number(parts[1])
    z = parse_number(parts[2])
    return tuple((x, y, z))


def main() -> None:
    print("=== Game Coordinate System ===")

    if len(sys.argv) == 4:
        origin = tuple((0, 0, 0))
        parsed = None
        try:
            position = parse_coordinates_string(sys.argv[1])
            print(f"\nPosition created: {position}")
            x1, y1, z1 = origin
            x2, y2, z2 = position
            dist1: float = float(math.sqrt((x2-x1)**2+(y2-y1)**2+(z2-z1)**2))
            print(f"Distance between {origin} and {position}: {dist1:.2f}\n")

            print(f"\nParsing coordinates: \"{sys.argv[2]}\"")
            parsed = parse_coordinates_string(sys.argv[2])
            print(f"Parsed position: {parsed}")
            x2, y2, z2 = parsed
            dist2: float = float(math.sqrt((x2-x1)**2+(y2-y1)**2+(z2-z1)**2))
            print(f"Distance between {origin} and {parsed}: {dist2:.1f}\n")

            print(f"\nParsing invalid coordinates: \"{sys.argv[3]}\"")
            parse_coordinates_string(sys.argv[3])
        except ValueError as err:
            print(f"Error parsing coordinates: {err}")
            print(f"Error details - Type: {err.__class__.__name__},"
                  f" Args: {err.args}")

        if parsed is not None:
            print("\nUnpacking demonstration:")
            x, y, z = parsed
            print(f"Player at x={x}, y={y}, z={z}")
            print(f"Coordinates: X={x}, Y={y}, Z={z}")
    else:
        print(f"No arguments provided. Usage: python3 "
              f"{sys.argv[0]} \"arg1\" \"arg2\" \"arg3\"")


if __name__ == "__main__":
    main()
