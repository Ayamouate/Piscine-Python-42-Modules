import sys
import math


def parse_number(value: str):
    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except ValueError:
            raise ValueError(f"'{value}' is an invalide number!")


def parse_coordinates_string(value: str) -> tuple:
    if ',' in value:
        parts: list[str] = value.split(',')
    else:
        parts: list[str] = value.split()
    if len(parts) != 3:
        raise ValueError(f"Expected 3 coordinates, got {len(parts)}!")
    x: int = parse_number(parts[0])
    y: int = parse_number(parts[1])
    z: int = parse_number(parts[2])
    return tuple((x, y, z))


def main() -> None:

    if len(sys.argv) == 4:
        print("=== Game Coordinate System ===")
        origin: tuple = tuple((0, 0, 0))
        try:
            parsed: list[int] = None
            position: tuple = parse_coordinates_string(sys.argv[1])
            print(f"\nPosition created: {position}")
            x1, y1, z1 = origin
            x2, y2, z2 = position
            dist1: float = float(math.sqrt((x2-x1)**2+(y2-y1)**2+(z2-z1)**2))
            print(f"Distance between {origin} and {position}: {dist1:.2f}")
        except ValueError as err:
            print(f"\nParsing invalid coordinates: \"{sys.argv[1]}\"")
            print(f"Error parsing coordinates: {err}")
            print(f"Error details - Type: {err.__class__.__name__},"
                  f" Args: {err.args}")

        for i in range(2, 4):
            try:
                coord: tuple = parse_coordinates_string(sys.argv[i])
                print(f"\nParsing coordinates: \"{sys.argv[i]}\"")
                print(f"Parsed position: {coord}")
                x, y, z = coord
                x1, y1, z1 = origin
                dist: float = float(math.sqrt((x-x1)**2+(y-y1)**2+(z-z1)**2))
                print(f"Distance between {origin} and {coord}: {dist:.1f}")
                if i == 2:
                    parsed = coord
            except ValueError as err:
                print(f"\nParsing invalid coordinates: \"{sys.argv[i]}\"")
                print(f"Error parsing coordinates: {err}")
                print(f"Error details - Type: {err.__class__.__name__},"
                      f" Args: {err.args}")

        if parsed is not None:
            print("\nUnpacking demonstration:")
            x, y, z = coord
            print(f"Player at x={x}, y={y}, z={z}")
            print(f"Coordinates: X={x}, Y={y}, Z={z}")
    else:
        print(f"Usage: python3 {sys.argv[0]} \"arg1\" \"arg2\" \"arg3\"")


if __name__ == "__main__":
    main()
